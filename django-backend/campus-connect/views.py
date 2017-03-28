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


class ListClubViewSet(viewsets.ModelViewSet, UpdateOnlyMixin):
    """
    All the clubs.
    """

    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    # update_serializer_class = UpdateClubSerializer


class ListStudentViewSet(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    """
    All the users
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ListEventViewSet(viewsets.ModelViewSet):
    """
    All the Events
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


'''
@csrf_exempt
def clubList(request):
    """
    
    get: Gives an error. POST is required.
    
    post: Returns a list of clubs
    
    """
    if request.method == 'POST':
        post_name = request.POST.get("name", "")
        clublist = Club.objects.filter(name__contains=post_name).values()
        response = JsonResponse({"status": SUCCESS_RESPONSE, 'clubs': list(clublist)})
    else:
        response = JsonResponse({"status": ERROR_RESPONSE, "detail": GET_NOT_ALLOWED_RESPONSE})

    return response


@csrf_exempt
def editUser(request):
    return JsonResponse({"status": ERROR_RESPONSE, "detail": NOT_IMPLEMENTED_ERROR})


@csrf_exempt
def addUser(request):
    return JsonResponse({"status": ERROR_RESPONSE, "detail": NOT_IMPLEMENTED_ERROR})



    URL: api/editclub/
    Type: POST
    Input Parameters:
        int id: The id of club you want to edit
        string token: The token that the user used to login. They must be an officer of the club to make changes to it.
        string name: Name of the club
        string email: Email of the club
        string meetingTimes: Times the club has regular meetings
        string website: Website of the club
    Output JSON:
        status: The status of the request.
        clubs: If status  = success, then this will be a list of dictionaries of the club(s) that were altered. This is a 
            list, despite expecting one result, to maintain consistency with all the other views.
        error: If status = error, this will explain the reason why.



@csrf_exempt
def editClub(request):
    if request.method == 'POST':
        post_id = request.POST.get("id", None)
        post_token = request.POST.get("token", None)
        if post_id == None:
            return JsonResponse({"status": ERROR_RESPONSE, "detail": "id not specified"})
        elif post_token == None:
            return JsonResponse({"status": ERROR_RESPONSE, "detail": "token not specified"})
        else:
            try:
                selected_club = Club.objects.get(id=post_id)
            except ObjectDoesNotExist:
                selected_club = None
            if selected_club == None:
                return JsonResponse({"status": ERROR_RESPONSE, "detail": "Club id " + str(post_id) + " does not exist"})

            user_id = getIDFromToken(post_token)
            if user_id == None:
                return JsonResponse({"status": ERROR_RESPONSE, "detail": "invalid token"})

            club_leaders = list()
            if selected_club.president != None:
                club_leaders.append(selected_club.president.id)
            if selected_club.treasurer != None:
                club_leaders.append(selected_club.treasurer.id)
            if selected_club.icc_rep != None:
                club_leaders.append(selected_club.icc_rep.id)

            if user_id in club_leaders:
                post_name = request.POST.get("name", None)
                post_email = request.POST.get("email", None)
                post_meeting_times = request.POST.get("meetingTimes", None)
                post_website = request.POST.get("website", None)

                Club.objects.filter(id=post_id) \
                    .update(name=post_name,
                            email=post_email,
                            meeting_times=post_meeting_times,
                            website=post_website)
                updated_club = Club.objects.filter(id=post_id).values()
                return JsonResponse({"status": SUCCESS_RESPONSE, 'clubs': list(updated_club)})

            else:
                return JsonResponse({"status": ERROR_RESPONSE, "detail": "user not authorized to edit club"})


    else:
        return JsonResponse({"status": ERROR_RESPONSE, "detail": GET_NOT_ALLOWED_RESPONSE})


"""
    URL: api/calendar/
    Type: POST
    Input Parameters:
        datetime afterDateTime: The time and date before the event starts
        datetime beforeDateTime: The time and date after the event ends
        string name: Filter for clubs containing this name
    Output JSON:
        status: The status of the request.
        calendar: If status  = success, then this will be a list of dictionaries of all the events.
        error: If status = error, this will explain the reason why.
"""


@csrf_exempt
def calendarList(request):
    if request.method == 'POST':
        post_after_datetime = request.POST.get("afterDateTime", None)
        post_before_datetime = request.POST.get("beforeDateTime", None)
        post_club_id = request.POST.get("clubName", None)

        if None in [post_after_datetime, post_before_datetime]:
            return JsonResponse(
                {"status": ERROR_RESPONSE, "detail": "Must specify afterDateTime, beforeDateTime"})

        calendar_list = Calendar.objects.values().filter(
            start_date_time__gte=post_before_datetime,
            end_date_time__gte=post_after_datetime)

        if None != post_club_id:
            calendar_list = calendar_list.filter(club=post_club_id)

        return JsonResponse({"status": SUCCESS_RESPONSE, 'calendar': list(calendar_list)})
    else:
        return JsonResponse({"status": ERROR_RESPONSE, "detail": GET_NOT_ALLOWED_RESPONSE})


@csrf_exempt
def addEditCalendar(request):
    return JsonResponse({"status": ERROR_RESPONSE, "detail": NOT_IMPLEMENTED_ERROR})


"""
    URL: api/users/
    Type: POST
    Input Parameters:
        int id: The id of the user
    Output JSON:
        status: The status of the request.
        detail: If status  = success, then this will be a list of dictionaries of users.
            id
            username
            first_name
            last_name
            email
        error: If status = error, this will explain the reason why.
"""


@csrf_exempt
def userList(request):
    if request.method == 'POST':
        post_id = request.POST.get("id", None)
        if post_id == None:
            return JsonResponse({"status": ERROR_RESPONSE, "detail": "id not specified"})

        users = StudentUser.objects.filter(id=post_id).values("id", "username", "first_name", "last_name", "email")
        return JsonResponse({"status": SUCCESS_RESPONSE, 'users': list(users)})
    else:
        return JsonResponse({"status": ERROR_RESPONSE, "detail": GET_NOT_ALLOWED_RESPONSE})
'''
