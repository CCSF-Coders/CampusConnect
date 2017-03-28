from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import admin


# This code is triggered whenever a new user has been created and saved to the database
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Club(models.Model):
    """
    Stores the general information for each Club
    :model:`campus-connect.Club`
    """
    name = models.CharField(max_length=64, default="")
    email = models.EmailField(max_length=128, blank=True, null=True)
    website = models.URLField(max_length=256, blank=True, null=True)
    meeting_times = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'campus-connect'


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    officer_of_club = models.ForeignKey(Club, related_name='officers', default=None, null=True, blank=True,)
    officer_role = models.CharField(max_length=64, default=None, null=True, blank=True,)
    member_of_clubs = models.ManyToManyField(Club, related_name='members', default=None, blank=True,)
    
    def __str__(self):
        return str(self.user)

    class Meta:
        app_label = 'campus-connect'
    
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.student.save()


class Event(models.Model):
    name = models.CharField(max_length=64, default="")
    description = models.CharField(max_length=512, default="", blank=True)
    club = models.ForeignKey(Club, related_name='president_of_club', default=None, null=True, blank=True)
    start_date_time = models.DateTimeField(default=None)
    end_date_time = models.DateTimeField(default=None)

    def __str__(self):
        return self.name + " at " + str(self.start_date_time)

    class Meta:
        app_label = 'campus-connect'


CUSTOM_MODELS = [Club, Event, Student, ]

admin.site.register(CUSTOM_MODELS)
