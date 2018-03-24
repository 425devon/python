from django.conf.urls import url, include
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    #url(r'^pickword$',views.pickword)
]