# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import SuperHero
# Create your views here.
def index(req):
    SuperHero.marvelManager.all()#<--only return me heros with universe="marvel"
    context = {
        "data" : SuperHero.objects.all() #[SuperHero, SuperHero] .validate
    }
    return render(req, "superheroes/index.html", context)

def new(req):
    return render(req, "superheroes/new.html")

def create(req):
    #validations
    isValid = SuperHero.objects.validate(req.POST)
    if isValid:
        SuperHero.objects.create(
            real_name = req.POST["real_name"],
            hero_name = req.POST["hero_name"],
            age = req.POST["age"],
            universe = req.POST["universe"]
        )
    else:
        messages.info(req, 'All inputs must be filled out')
    return redirect("/superheroes/new")

