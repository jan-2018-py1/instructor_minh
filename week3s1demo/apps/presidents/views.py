# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import President
from django.contrib import messages

# Create your views here.
def index(req):
    context = {
        "all_pres" : President.objects.all() #[President, President, President]
    }
    return render(req, "presidents/index.html", context)

def new(req):
    return render(req, "presidents/new.html")

def create(req):
    if req.method == "POST":
        isValid =  President.objects.validate(req.POST)
        if isValid:
            President.objects.create(first_name=req.POST["first_name"], last_name=req.POST["last_name"], motto=req.POST["motto"], start_term=req.POST["start_year"], end_term=req.POST["end_year"])
            return redirect("/presidents/new")
        else:
            messages.error(req, 'All inputs must be filled')
            return redirect("/presidents/new")