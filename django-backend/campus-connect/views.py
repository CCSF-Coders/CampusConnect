from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from . import models
from django.views.decorators.csrf import csrf_exempt
# from .forms import UserForm
from .models import Club, User
from django.core import serializers
from django.forms.models import model_to_dict

GET_NOT_ALLOWED_RESPONSE = "Method \"GET\" not allowed."
ERROR_RESPONSE = "error"
SUCCESS_RESPONSE = "success"

# Homepage of website
def index(request):
    return render(request, 'index_example.html')

# Get a list of clubs
@csrf_exempt
def clublist(request):
    response = None
    if request.method == 'POST':
        clublist = Club.objects.values()
        response = JsonResponse({"status": SUCCESS_RESPONSE, 'clubs': list(clublist)})
    else:
        response = JsonResponse({"status": ERROR_RESPONSE , "detail": GET_NOT_ALLOWED_RESPONSE})

    return response