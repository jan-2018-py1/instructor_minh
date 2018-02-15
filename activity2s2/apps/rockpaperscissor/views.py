# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(req):
    if "player_wins" not in req.session:
        req.session["player_wins"] = 0
        req.session["comp_wins"] = 0
        req.session["draw_count"] = 0
    context = {
        "comp_score": req.session["comp_wins"],
        "player_score": req.session["player_wins"],
        "draw_count":req.session["draw_count"]
    }
    return render(req, "rockpaperscissor/index.html", context)

def choice(req, choice):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3
    computer_choice = random.randint(1,3)
    if choice == "rock":
        player_choice = ROCK
    elif choice == "paper":
        player_choice = PAPER
    elif choice == "scissor":
        player_choice = SCISSOR
    else:
        player_choice = requst.POST["choice"]

    if computer_choice == ROCK:
        if player_choice == ROCK:
            req.session["draw_count"] += 1
        elif player_choice == PAPER:
            req.session["player_wins"] += 1
        else:
            req.session["comp_wins"] += 1
    elif computer_choice == PAPER:
        if player_choice == PAPER:
            req.session["draw_count"] += 1
        elif player_choice == SCISSOR:
            req.session["player_wins"] += 1
        else:
            req.session["comp_wins"] += 1
    elif computer_choice == SCISSOR:
        if player_choice == SCISSOR:
            req.session["draw_count"] += 1
        elif player_choice == ROCK:
            req.session["player_wins"] += 1
        else:
            req.session["comp_wins"] += 1
    #DECIDE who wins, update session
    return redirect("/rockpaperscissor")