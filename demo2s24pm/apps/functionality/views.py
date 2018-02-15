# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(req):
    return HttpResponse("hello")

def showIndex(req):
    if "first_name" in req.session:
        name = req.session["first_name"]
    else:
        name = "Minh"
    context = {
        "name":name,
        "age":25,
        "hobbies":["sports", "coding", "finance"],
        "students":[{"name":"greg", "location":"Portland, OR"}, {"name":"todd", "location":"Tulsa, OK"}, {"name":"garrett", "location":"Salinas, CA"}]
    }
    return render(req, "functionality/index.html", context)

def hello(req, student_name):
    return HttpResponse(student_name)

def process(req):
    req.session["first_name"] = req.POST["first_name"]
    return redirect("/functionality/index")