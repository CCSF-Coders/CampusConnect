from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

from django.contrib import admin


# This code is triggered whenever a new user has been created and saved to the database
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Club(models.Model):
    name = models.CharField(max_length=64, default="")
    email = models.EmailField(max_length=128, blank=True, null=True)
    website = models.URLField(max_length=256, blank=True, null=True)
    meeting_times = models.CharField(max_length=256, blank=True, null=True)

    # officers that can manage the club
    president = models.ForeignKey(User, related_name='president_of_club', default=None, null=True, blank=True)
    treasurer = models.ForeignKey(User, related_name='treasurer_of_club', default=None, null=True, blank=True)
    icc_rep = models.ForeignKey(User, related_name='icc_rep_of_club', default=None, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'campus-connect'


class Calendar(models.Model):
    name = models.CharField(max_length=64, default="")
    description = models.CharField(max_length=512, default="", blank=True)
    club = models.ForeignKey(Club, related_name='president_of_club', default=None, null=True, blank=True)
    start_date_time = models.DateTimeField(default=None)
    end_date_time = models.DateTimeField(default=None)

    def __str__(self):
        return self.name + " at " + str(self.start_date_time)

    class Meta:
        app_label = 'campus-connect'
        
CUSTOM_MODELS = [Club, Calendar]

admin.site.register(CUSTOM_MODELS)