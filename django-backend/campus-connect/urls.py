"""campus-connect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views
from rest_framework.authtoken import views as rest_views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
    # url(r'^api/register/', views.register),

    url(r'^api/clubs/', views.clubList),
    url(r'^api/editclub/', views.editClub),

    url(r'^api/calendar/', views.calendarList),
    url(r'^api/editcalendar/', views.addEditCalendar),

    url(r'^api/users/', views.userList),
    url(r'^api/edituser/', views.editUser),
    url(r'^api/adduser/', views.addUser),

    url(r'^api/token/', rest_views.obtain_auth_token),
]
