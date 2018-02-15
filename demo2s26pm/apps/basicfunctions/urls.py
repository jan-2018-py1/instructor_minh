
from django.conf.urls import url
import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^hello$', views.hello),
    url(r'^process_form$', views.process),
    url(r'^hello/(?P<student_name>\w+)$', views.helloName),    
    
]
