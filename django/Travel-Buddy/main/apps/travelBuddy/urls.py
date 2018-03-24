from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
url(r'^$', views.index),
url(r'^add$', views.add),
url(r'^newTrip$', views.newTrip),
url(r'^logout$', views.clear),
url(r'^destination/(?P<id>\d+)$',views.destination),
url(r'^join/(?P<id>\d+)$',views.join),
]