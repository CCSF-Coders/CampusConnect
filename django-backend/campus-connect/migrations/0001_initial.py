# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 16:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=64)),
                ('description', models.CharField(blank=True, default='', max_length=512)),
                ('start_date_time', models.DateTimeField(default=None)),
                ('end_date_time', models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=64)),
                ('email', models.EmailField(blank=True, max_length=128, null=True)),
                ('website', models.URLField(blank=True, max_length=256, null=True)),
                ('meeting_times', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('officer_role', models.CharField(default=None, max_length=64, null=True)),
                ('officer', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='officer_of_club', to='campus-connect.Club')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='calendar',
            name='club',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='president_of_club', to='campus-connect.Club'),
        ),
    ]
