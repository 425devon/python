from django.conf.urls import url, include
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^home$',views.home),
    url(r'^farm$',views.farm),
    url(r'^cave$',views.cave),
    url(r'^house$',views.house),
    url(r'^casino$',views.casino),
]