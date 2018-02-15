
from django.conf.urls import url
from django.contrib import admin
import views
# /rockpaperscissor
# /rockpaperscissor/<choice>
urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<choice>\w+)$', views.choice)
]