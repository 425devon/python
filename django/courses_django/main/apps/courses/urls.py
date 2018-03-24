from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
url(r'^$', views.index),     # This line has changed!
url(r'^create$', views.create),
url(r'^remove/(?P<id>\d+)$', views.remove),
url(r'^destroy/(?P<id>\d+)$', views.destroy)
]
