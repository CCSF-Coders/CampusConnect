from .models import Club, Student, Event, Token
from django.contrib.auth.models import User, Group
from rest_framework import serializers, exceptions
from django.core.exceptions import ObjectDoesNotExist


def isOfficerOfClub(token, club):
    """
        :param str token: The user's token
        :param Club club: The club to check the user is an officer of
        :return: True if they are an officer, False if they are not an officer, and None if the token was not found.
        :rtype: bool 
    """
    try:
        student = Token.objects.get(key=token).user.student  # type: Student
        return club == student.officer_of_club
    except ObjectDoesNotExist:
        return None


def isStaffOfSite(token):
    """
        :param str token: user's token
        :return: True if they are staff, False if they are not staff, and None if the token was not found.
        :rtype: bool 
    """
    try:
        return Token.objects.get(key=token).user.is_staff
    except ObjectDoesNotExist:
        return None


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
    token = serializers.CharField(write_only=True)
    name = Club.name

    class Meta:
        model = Club
        fields = '__all__'

    def update(self, instance, validated_data):
        '''        
        :type instance: Club
        :type validated_data: dict
        '''

        officer_status = isOfficerOfClub(validated_data['token'], instance)

        if officer_status is True:
            instance.name = validated_data.get('name', instance.name)
            instance.email = validated_data.get('email', instance.email)
            instance.website = validated_data.get('website', instance.website)
            instance.meeting_times = validated_data.get('meeting_times', instance.meeting_times)
            instance.save()
        elif officer_status is False:
            raise exceptions.AuthenticationFailed(detail="Not an officer of the club", code=None)
        elif officer_status is None:
            raise exceptions.AuthenticationFailed(detail="User does not exist", code=None)

    def create(self, validated_data):
        '''        
        :type validated_data: dict
        '''

        staff_status = isStaffOfSite(validated_data['token'])
        if staff_status is True:
            validated_data.pop('token')
            return Club.objects.create(**validated_data)
        elif staff_status is False:
            raise exceptions.AuthenticationFailed(detail="User is not staff", code=None)
        elif staff_status is None:
            raise exceptions.AuthenticationFailed(detail="User does not exist", code=None)


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

        officer_status = isOfficerOfClub(validated_data['token'], club)

        if officer_status is True:
            instance.name = validated_data.get('name', instance.name)
            instance.description = validated_data.get('description', instance.description)
            instance.club_id = validated_data.get('club_id', instance.club)
            instance.start_date_time = validated_data.get('start_date_time', instance.start_date_time)
            instance.end_date_time = validated_data.get('end_date_time', instance.end_date_time)
            instance.save()
        elif officer_status is False:
            raise exceptions.AuthenticationFailed(detail="Not an officer of the club", code=None)
        elif officer_status is None:
            raise exceptions.AuthenticationFailed(detail="User does not exist", code=None)

    def create(self, validated_data):
        '''        
        :type validated_data: dict
        '''

        validated_data['club'] = Club.objects.get(id=validated_data['club_id'])
        validated_data.pop('club_id')

        officer_status = isOfficerOfClub(validated_data['token'], validated_data['club'])

        if officer_status is True:
            validated_data.pop('token')
            return Event.objects.create(**validated_data)
        elif officer_status is False:
            raise exceptions.AuthenticationFailed(detail="Not an officer of the club", code=None)
        elif officer_status is None:
            raise exceptions.AuthenticationFailed(detail="User does not exist", code=None)
