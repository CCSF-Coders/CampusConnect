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
from django.views.decorators.cache import cache_page
from django.conf import settings

router = DefaultRouter()

router.register(r'clubs', views.ClubViewSet, 'List and Edit Clubs')
router.register(r'students', views.StudentViewSet, 'List and Edit Students')
router.register(r'events', views.EventViewSet, 'List and Edit Events')

urlpatterns = [

    url(r'^$', cache_page(1)(views.index), name="Homepage"),
    url(r'^admin/', admin.site.urls),
    url(r'^rest-api/', include(router.urls), name="Rest API"),
    url(r'^token/', rest_views.obtain_auth_token, name="User Token (login)"),
    url(r'^docs/', include_docs_urls()),
    #url(r'', cache_page(1)(views.IndexView.as_view()), name='index'),

]
