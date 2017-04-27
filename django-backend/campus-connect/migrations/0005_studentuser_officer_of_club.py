# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 17:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campus-connect', '0004_remove_studentuser_officer_of_club'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentuser',
            name='officer_of_club',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='officer_of_club', to='campus-connect.Club'),
        ),
    ]
