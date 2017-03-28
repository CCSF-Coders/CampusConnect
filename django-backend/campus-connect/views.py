from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from . import models
from django.views.decorators.csrf import csrf_exempt
# from .forms import UserForm
from .models import Club, Token, Event, Student
from django.contrib.auth.models import User
from django.core import serializers
from django.forms.models import model_to_dict
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, permissions, mixins
from rest_framework.response import Response
from .serializers import ClubSerializer, UserSerializer, StudentSerializer, EventSerializer
from .mixins import UpdateOnlyMixin

GET_NOT_ALLOWED_RESPONSE = "Method \"GET\" not allowed."
ERROR_RESPONSE = "error"
SUCCESS_RESPONSE = "success"
NOT_IMPLEMENTED_ERROR = "feature not implemented yet"


def index(request):
    """
    The homepage of the website.
    :view:`campus-connect.index`
    """
    return render(request, 'index.html')
    # return render(request, 'index_example.html')


'''
    The definition of ModelViewSet is:

    class ModelViewSet(mixins.CreateModelMixin, 
                       mixins.RetrieveModelMixin, 
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.ListModelMixin,
                       GenericViewSet)

    Use whatever you need
'''


class ClubViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """
    This is how data about Clubs is accessed
    
    GET:
    /rest-api/clubs
    This will list all the clubs if no parameters are specified.
    optional params: name (contains)
    e.g. /rest-api/clubs/?name=coders
    
    POST:
    /rest-api/clubs
    This will create a club if the user is flagged as staff.
    required params: token, name
    optional params: email, website, meeting times
    
    POST:
    /rest-api/clubs/<club_id>
    This will update a club if the user is flagged as staff or an officer of that club.
    required params: token
    optional params: name, email, website, meeting_times  
    
    """

    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    search_fields = ('name',)

    def get_queryset(self):
        """
        Allows filtering of the data
        """
        queryset = Club.objects.all()
        name = self.request.query_params.get('name', None)

        if name is not None:
            queryset = queryset.filter(name__contains=name)

        return queryset


class StudentViewSet(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    """
     This will list the Students. The Students is a table that has a One-to-One relationship with the Users table.
     Students and Users have their own separate ids.

     GET:
     /rest-api/students
     This will list all the clubs if no parameters are specified.
     optional params: username, email, first_name (contains), last_name (contains)
     e.g. /rest-api/students/?first_name=ryan
     
     """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        """
        Allows filtering of the data
        """
        queryset = Student.objects.all()
        username = self.request.query_params.get('username', None)
        email = self.request.query_params.get('email', None)
        first_name = self.request.query_params.get('first_name', None)
        last_name = self.request.query_params.get('last_name', None)

        if username is not None:
            queryset = queryset.filter(user__username=username)
        if email is not None:
            queryset = queryset.filter(user__email=email)
        if first_name is not None:
            queryset = queryset.filter(user__first_name__contains=first_name)
        if last_name is not None:
            queryset = queryset.filter(user__last_name__contains=last_name)

        return queryset


class EventViewSet(viewsets.ModelViewSet):
    """
    This is how data about Events is accessed

    GET:
    /rest-api/events
    This will list all the events if no parameters are specified. Specifying a start_date will filter for events that
    start after that date and time, and specifying an end_date will filter for events that end after that date and time.
    optional params: club_id, start_date, end_date
    e.g. /rest-api/events/?start_date=2017-03-29&end_date=2017-03-29

    POST:
    /rest-api/events
    This will create an event if the user is flagged as staff or an officer of that club.
    required params: token, club_id, name, start_date, end_date
    optional params: description

    POST:
    /rest-api/events/<event_id>
    This will update an event if the user is flagged as staff or an officer of that club.
    required params: token
    optional params: name, email, website, meeting_times  

    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        """
        Allows filtering of the data
        """
        queryset = Event.objects.all()
        club_id = self.request.query_params.get('club_id', None)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)

        if club_id is not None:
            queryset = queryset.filter(club_id=club_id)
        if start_date is not None:
            queryset = queryset.filter(start_date_time__gt=start_date)
        if end_date is not None:
            queryset = queryset.filter(end_date_time__lt=end_date)

        return queryset
