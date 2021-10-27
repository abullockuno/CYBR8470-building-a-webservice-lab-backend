from __future__ import unicode_literals

from django.db import models
from django.core.validators import *

from django.contrib.auth.models import User, Group

from django.contrib import admin
import base64

class Event(models.Model):
    eventtype = models.CharField(max_length=1000, blank=False)
    timestamp = models.DateTimeField()
    userid = models.CharField(max_length=1000, blank=True)
    requestor = models.GenericIPAddressField(blank=False)

    def __str__(self):
        return str(self.eventtype)

class EventAdmin(admin.ModelAdmin):
    list_display = ('eventtype', 'timestamp')

class ApiKey(models.Model):
    owner = models.CharField(max_length=1000, blank=False)
    key = models.CharField(max_length=5000, blank=False)

    def __str__(self):
        return str(self.owner) + str(self.key)

class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('owner','key')

class Breed(models.Model):
    TINY = 'TN'
    SMALL = 'SM'
    MEDIUM = 'MD'
    LARGE = 'LG'
    SIZE_CHOICES = [
        ('TN', 'Tiny'),
        ('SM', 'Small'),
        ('MD', 'Medium'),
        ('LG', 'Large'),
    ]
    VALUE_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    name = models.CharField(max_length=1000, blank=False)
    size = models.CharField(
        max_length = 2,
        choices = SIZE_CHOICES,
        default = MEDIUM,
    )
    friendliness = models.IntegerField(
        choices = VALUE_CHOICES,
        default = 3,
    )
    trainability = models.IntegerField(
        choices = VALUE_CHOICES,
        default = 3,
    )
    sheddingamount = models.IntegerField(
        choices = VALUE_CHOICES,
        default = 3,
    )
    exerciseneeds = models.IntegerField(
        choices = VALUE_CHOICES,
        default = 3,
    )


class Dog(models.Model):

    name = models.CharField(max_length=1000, blank=False)
    age = models.IntegerField(blank=False)
    breed = models.ForeignKey(
        Breed,
        on_delete=models.CASCADE
    )
    gender = models.CharField(max_length=1000, blank=True)
    color = models.CharField(max_length=1000, blank=True)
    favoritefood = models.CharField(max_length=1000, blank=True)
    favoritetoy = models.CharField(max_length=1000, blank=True)
