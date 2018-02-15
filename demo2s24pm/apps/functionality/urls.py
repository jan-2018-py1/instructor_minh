from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index$', views.showIndex),
    url(r'^hello/(?P<student_name>\w+)$', views.hello),
    url(r'^process_form$', views.process),
    
]