from django.conf.urls import url, include
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$',views.newUser),
    url(r'^create$', views.create),
    url(r'^(?P<id>\d+)$',views.show),
    url(r'^(?P<id>\d+)/edit$',views.edit),
    url(r'^(?P<id>\d+)/update$',views.update),
    url(r'^(?P<id>\d+)/destroy$',views.delete),
]