from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from . import models
from django.views.decorators.csrf import csrf_exempt
# from .forms import UserForm
from .models import Club, User, Token, Calendar
from django.core import serializers
from django.forms.models import model_to_dict
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

GET_NOT_ALLOWED_RESPONSE = "Method \"GET\" not allowed."
ERROR_RESPONSE = "error"
SUCCESS_RESPONSE = "success"
NOT_IMPLEMENTED_ERROR = "feature not implemented yet"


# returns None if token is a mismatch
def getIDFromToken(id):
    try:
        token_search = Token.objects.get(key=id)
        token = token_search.user_id
    except ObjectDoesNotExist:
        token = None

    return token


# Homepage of website
def index(request):
    return render(request, 'index.html')
    # return render(request, 'index_example.html')


# Get a list of clubs
@csrf_exempt
def clubList(request):
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


@csrf_exempt
def calendarList(request):
    if request.method == 'POST':
        post_after_datetime = request.POST.get("afterDateTime", None)
        post_before_datetime = request.POST.get("beforeDateTime", None)
        post_club_name = request.POST.get("clubName", None)

        if (None in [post_after_datetime, post_before_datetime, post_club_name]):
            return JsonResponse(
                {"status": ERROR_RESPONSE, "detail": "Must specify afterDateTime, beforeDateTime, and clubName"})

        calendar_list = Calendar.objects.values().filter(club__name__contains=post_club_name,
                                                         start_date_time__gte=post_after_datetime,
                                                         end_date_time__gte=post_before_datetime)
        return JsonResponse({"status": SUCCESS_RESPONSE, 'calendar': list(calendar_list)})
    else:
        return JsonResponse({"status": ERROR_RESPONSE, "detail": GET_NOT_ALLOWED_RESPONSE})


@csrf_exempt
def addEditCalendar(request):
    return JsonResponse({"status": ERROR_RESPONSE, "detail": NOT_IMPLEMENTED_ERROR})


@csrf_exempt
def userList(request):
    if request.method == 'POST':
        post_id = request.POST.get("id", None)
        if post_id == None:
            return JsonResponse({"status": ERROR_RESPONSE, "detail": "id not specified"})

        users = User.objects.filter(id=post_id).values("id", "username", "first_name", "last_name", "email")
        return JsonResponse({"status": SUCCESS_RESPONSE, 'users': list(users)})
    else:
        return JsonResponse({"status": ERROR_RESPONSE, "detail": GET_NOT_ALLOWED_RESPONSE})
