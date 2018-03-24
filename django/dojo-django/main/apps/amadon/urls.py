from django.conf.urls import url, include
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^checkout$',views.checkout),
    url(r'^shirt$',views.shirt),
    url(r'^sweater$',views.sweater),
    url(r'^cup$',views.cup),
    url(r'^book$',views.book),
]