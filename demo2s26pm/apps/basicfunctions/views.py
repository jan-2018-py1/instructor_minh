# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def index(req):
    return HttpResponse("got here")
    
def hello(req):
    if "first_name" in req.session:
        name = req.session["first_name"]
    else:
        name = "Minh"
    context = {
        "name":name,
        "favorite_numbers":[7,13,25],
        "students":[
            {"name":"joel", "occupation":"Student"},
            {"name":"Daniel", "occupation":"Student"},
            {"name":"Jasper", "occupation":"Student"},
        ]
    }
    return render(req, "basicfunctions/index.html", context)
    
def process(req):
    if req.method == "POST":
        req.session["first_name"] = req.POST["first_name"]
        return HttpResponse(req.POST["first_name"])
    else:
        return redirect("/")

def helloName(req, student_name):
    return HttpResponse(student_name)
    