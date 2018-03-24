from django.conf.urls import url, include
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$',views.process),
    url(r'^back$',views.back)
]