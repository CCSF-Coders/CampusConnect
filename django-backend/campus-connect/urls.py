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
from rest_framework.documentation import include_docs_urls
from django.conf.urls import include
from rest_framework.authtoken import views as rest_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'list-clubs', views.ListClubViewSet, 'View Clubs')
router.register(r'list-students', views.ListStudentViewSet, 'View Students')
router.register(r'list-events', views.ListEventViewSet, 'View Events')

#router.register(r'edit-clubs', views.EditClubViewSet, 'Edit Clubs')
#router.register(r'edit-users', views.EditUserViewSet, 'Edit Users')


urlpatterns = [

    url(r'^$', views.index, name="Homepage"),
    url(r'^admin/', admin.site.urls),
    url(r'^rest-api/', include(router.urls), name="Rest API"),
    url(r'^token/', rest_views.obtain_auth_token, name="User Token (login)"),
    url(r'^docs/', include_docs_urls()),
    # url(r'^rest-apiT/clubs', views.ClubViewSet.as_view()),
    # url(r'^rest-apiT/users', views.UserViewSet.as_view()),

    # url(r'^api/register/', views.register),

    # url(r'^api/', include('campus-connect.urls_api', namespace="campus-connect:api")),
]
