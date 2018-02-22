# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Wrestler
# Create your views here.
def index(req):
    context = {
        "wrestlers": Wrestler.objects.all()
    }
    return render(req, 'wrestlers/index.html', context)

def create():
    name = request.form['name'],
    weight = request.form['weight'],
    nick_name = request.form['nick_name']
    Wrestler.objects.create(name=name, weight=weight, nick_name=nick_name)
    return redirect('/wrestlers')

def edit(req, wrestler_id):
    context = {
        "wrestler": Wrestler.objects.get(id=wrestler_id)
    }
    return render(req, "wrestlers/edit.html", context)
def show(req, wrestler_id):
    context = {
        "wrestler": Wrestler.objects.get(id=wrestler_id)
    }
    return render("wrestlers/show.html", context)

def update(req, wrestler_id):
    wrestler = Wrestler.objects.get(id=wrestler_id)
    wrestler.name = request.form['name'],
    wrestler.weight = request.form['weight'],
    wrestler.nick_name = request.form['nick_name']
    wrestler.save()
    return redirect('/')
def new(req):
    return render(req, "wrestlers/new.html")
def destroy(req, wrestler_id):
    Wrestler.objects.get(id=wrestler_id).delete()
    return redirect('/')
