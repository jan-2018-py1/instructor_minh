# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random

from django.shortcuts import render, HttpResponse

# Create your views here.
def index(req):

    return render(req, 'rock_paper_scissor/index.html')

def choice(req, choice):
    #random guess from computer
    
    computer_guess = {
        '1' : rock,
        '2' : paper,
        '3' : scissor,
    }
    
    return redirect('rock_paper_scissor/')
