from .models import Club, Student, Event, Token
from django.contrib.auth.models import User, Group
from rest_framework import serializers, exceptions
from django.core.exceptions import ObjectDoesNotExist


def validateTokenWithStudent(token, student):
    """
    
    :param str token: 
    :param Student student: 
    :return: 
    """
    try:
        token_student = Token.objects.get(key=token).user.student  # type: Student
        if token_student == student:
            return True
        else:
            raise exceptions.AuthenticationFailed(detail="Token Error: Doesn't match the Student you are trying to edit", code=None)
    except ObjectDoesNotExist:
        raise exceptions.AuthenticationFailed(detail="Token Error: User does not exist", code=None)


def validateOfficer(token, club):
    """
    This will check if the user is an officer of the specified club. 
    If they are not, it will raise an AuthenticationFailed exception.
    
    :param str token: The user's token
    :param Club club: The club to check the user is an officer of
    :return: True if they are an officer.
    :rtype: bool
    :raises: AuthenticationFailed
    """

    try:
        student = Token.objects.get(key=token).user.student  # type: Student
        if club == student.officer_of_club:
            return True
        else:
            raise exceptions.AuthenticationFailed(detail="Token Error: Not an officer of the club", code=None)
    except ObjectDoesNotExist:
        raise exceptions.AuthenticationFailed(detail="Token Error: User does not exist", code=None)


def validateStaff(token):
    """
    This will check if the user is staff. If they are not, it will raise an AuthenticationFailed exception.
    
    :param str token: user's token
    :return: True if they are staff.
    :rtype: bool
    :raises: AuthenticationFailed
    """
    try:
        if Token.objects.get(key=token).user.is_staff:
            return True
        else:
            raise exceptions.AuthenticationFailed(detail="Token Error: The user is not staff", code=None)
    except ObjectDoesNotExist:
        raise exceptions.AuthenticationFailed(detail="Token Error: User does not exist", code=None)


def validateOfficerOrStaff(token, club):
    """
    This will check if the user is an officer of the specified club, or if they are staff. 
    If they are not, it will raise an AuthenticationFailed exception.

    :param str token: The user's token
    :param Club club: The club to check the user is an officer of
    :return: True if they are an officer or staff.
    :rtype: bool
    :raises: AuthenticationFailed
    """
    try:
        student = Token.objects.get(key=token).user.student  # type: Student
        if club == student.officer_of_club or Token.objects.get(key=token).user.is_staff:
            return True
        else:
            raise exceptions.AuthenticationFailed(detail="Token Error: Not an officer of the club", code=None)
    except ObjectDoesNotExist:
        raise exceptions.AuthenticationFailed(detail="Token Error: User does not exist", code=None)


def getStudent(id):
    try:
        return Student.objects.get(id=id)
    except ObjectDoesNotExist:
        raise exceptions.AuthenticationFailed(detail="Student \"" + str(id) + "\" does not exist", code=None)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email',)


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    token = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Student
        fields = '__all__'

    def update(self, instance, validated_data):
        '''        
        :type instance: Student
        :type validated_data: dict
        '''

        validateTokenWithStudent(validated_data['token'], instance)
        validated_data.pop('token')

        return super(StudentSerializer, self).update(instance, validated_data)


class BaseClubSerializer(serializers.ModelSerializer):
    token = serializers.CharField(write_only=True, required=True)
    name = Club.name
    add_officer = serializers.IntegerField(write_only=True, required=False)
    remove_officer = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Club
        fields = '__all__'

    def update(self, instance, validated_data):
        '''        
        :type instance: Club
        :type validated_data: dict
        '''

        validateOfficerOrStaff(validated_data['token'], instance)
        validated_data.pop('token')

        if 'add_officer' in validated_data:
            student_to_add = getStudent(validated_data['add_officer'])
            instance.officers.add(student_to_add)
            validated_data.pop('add_officer', None)

        if 'remove_officer' in validated_data:
            student_to_add = getStudent(validated_data['remove_officer'])
            instance.officers.add(student_to_add)
            validated_data.pop('remove_officer', None)

        return super(BaseClubSerializer, self).update(instance, validated_data)

    def create(self, validated_data):
        '''        
        :type validated_data: dict
        '''

        validateStaff(validated_data['token'])
        validated_data.pop('token', None)
        validated_data.pop('add_officer', None)
        validated_data.pop('remove_officer', None)

        return super(BaseClubSerializer, self).create(validated_data)


class ClubSerializer(BaseClubSerializer):
    officers = StudentSerializer(many=True, read_only=True)
    members = StudentSerializer(many=True, read_only=True)


class EventSerializer(serializers.ModelSerializer):
    token = serializers.CharField(write_only=True)
    club = BaseClubSerializer(read_only=True)
    club_id = serializers.IntegerField(required=True, write_only=True)

    class Meta:
        model = Event
        fields = '__all__'

    def update(self, instance, validated_data):
        '''        
        :type instance: Event
        :type validated_data: dict
        '''

        club = Club.objects.get(id=instance.club.id)
        validateOfficerOrStaff(validated_data['token'], club)
        validated_data.pop('token')

        return super(EventSerializer, self).update(instance, validated_data)

    def create(self, validated_data):
        '''        
        :type validated_data: dict
        '''

        validated_data['club'] = Club.objects.get(id=validated_data['club_id'])
        validateOfficerOrStaff(validated_data['token'], validated_data['club'])
        validated_data.pop('token')
        validated_data.pop('club_id')

        return super(EventSerializer, self).create(validated_data)
