from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^presidents$', views.index),
    url(r'^presidents/new$', views.new),
    url(r'^presidents/create$', views.create)
    
]
