from django.http import HttpResponse
from django.shortcuts import render
from . import models

def index(request):
    return render(request, 'index.html')