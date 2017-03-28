'''from django.conf.urls import url
from . import views
from rest_framework.authtoken import views as rest_views

urlpatterns = [
    url(r'^clubs/', views.clubList, name="Club List"),
    url(r'^editclub/', views.editClub, name="Edit Club"),

    url(r'^calendar/', views.calendarList, name="Calendar"),
    url(r'^editcalendar/', views.addEditCalendar, name="Edit Calendar"),

    url(r'^users/', views.userList, name="User List"),
    url(r'^edituser/', views.editUser, name="Edit User"),
    url(r'^adduser/', views.addUser, name="Add User (registration)"),

    url(r'^token/', rest_views.obtain_auth_token, name="User Token (login)"),
]
'''