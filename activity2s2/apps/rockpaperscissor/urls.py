from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^rockpaperscissor/$', views.index),
    url(r'^rockpaperscissor/(?P<choice>\w+)$', views.choice),
    
    #need another route here
]