from django.conf.urls import url
import views
urlpatterns = [
    url(r'^wrestlers$', views.index),
    url(r'^wrestlers/new$', views.new),#html page
    url(r'^wrestlers/create$', views.create),
    url(r'^wrestlers/(?P<wrestlers_id>\d+)', views.show),
    url(r'^wrestlers/(?P<wrestlers_id>\d+)/edit', views.edit),
    url(r'^wrestlers/(?P<wrestlers_id>\d+)/update', views.update),
    url(r'^wrestlers/(?P<wrestlers_id>\d+)/delete', views.destroy),
]