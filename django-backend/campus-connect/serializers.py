from .models import Club, Student, Event, Token
from django.contrib.auth.models import User, Group
from rest_framework import serializers, exceptions
from django.core.exceptions import ObjectDoesNotExist


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
            raise exceptions.AuthenticationFailed(detail="Not an officer of the club", code=None)
    except ObjectDoesNotExist:
        raise exceptions.AuthenticationFailed(detail="User does not exist", code=None)


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
            raise exceptions.AuthenticationFailed(detail="The user is not staff", code=None)
    except ObjectDoesNotExist:
        raise exceptions.AuthenticationFailed(detail="User does not exist", code=None)


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
            raise exceptions.AuthenticationFailed(detail="Not an officer of the club", code=None)
    except ObjectDoesNotExist:
        raise exceptions.AuthenticationFailed(detail="User does not exist", code=None)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email',)


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = '__all__'


class BaseClubSerializer(serializers.ModelSerializer):
    token = serializers.CharField(write_only=True, required=True)
    name = Club.name

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
        return super(BaseClubSerializer, self).update(instance, validated_data)

    def create(self, validated_data):
        '''        
        :type validated_data: dict
        '''

        validateStaff(validated_data['token'])
        validated_data.pop('token')
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

        club = Club.objects.get(id=instance.club_id)
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
