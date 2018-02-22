from django.conf.urls import url
import views 

urlpatterns = [
    url(r'^superheroes$', views.index),
    url(r'^superheroes/new$', views.new), #displays HTML
    url(r'^superheroes/create$', views.create), #Handle POST
]
