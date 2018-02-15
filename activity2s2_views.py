# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random

Rock = 1
Paper = 2
Scissor = 3

def index(req):

    return render(req, "rockpaperscissor/index.html")


def choice(req, choice):
    rand = random.randint(1,3)
    if rand == 1 and req.POST['rock']:
        tie
    elif rand == 2 and req.POST['rock']:

    elif rand == 3 and req.POST['rock']:

    elif rand == 2 and req.POST['']
