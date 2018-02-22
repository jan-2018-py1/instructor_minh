# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class PresidentManager(models.Manager): #.all, .create, .filter, .validate
    def validate(self, data):
        for key in data:
            if data[key] == "":
                return False
        return True
#object <---base python object
#__dict__
#__class__

class President(models.Model): #inherited the base 'objects' manager 
    first_name = models.CharField(max_length=255) 
    last_name = models.CharField(max_length=255)
    motto = models.TextField(default="")
    start_term = models.IntegerField()
    end_term = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PresidentManager()

    def display(self):
        return "{} {} - '{}'".format(self.last_name, self.first_name, self.motto)

class FirstLady(models.Model):
    president = models.ForeignKey(President, related_name="first_ladies")
    first_name = models.CharField(max_length=255) 
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Mistress(models.Model): #inherited the base 'objects' manager
    first_name = models.CharField(max_length=255) 
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Scandal(models.Model): #inherited the base 'objects' manager
    mistress = models.ForeignKey(Mistress, related_name="scandals")
    president = models.ForeignKey(President, related_name="scandals")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

