# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class SuperHeroManager(models.Manager):
    def validate(self, data):
        for key in data:
            if data[key] == "":
                return False
        return True
# Create your models here.
class SuperHero(models.Model):
    real_name = models.CharField(max_length=255)
    hero_name = models.CharField(max_length=255)
    age = models.IntegerField()
    universe = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = SuperHeroManager()

    def display_name(self):
        return "{} ({}) ".format(self.real_name, self.hero_name)

class Vehicle(models.Model):
    title = models.CharField(max_length=255)
    superHero = models.ForeignKey(SuperHero, related_name="vehicles")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Power(models.Model):
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class HeroPower(models.Model):
    power = models.ForeignKey(Power, related_name="heros")
    superHero = models.ForeignKey(SuperHero, related_name="powers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#speed
# Power.objects.get(id=1).heros