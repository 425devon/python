from django.conf.urls import url, include
from . import views           # This line is new!
urlpatterns = [
url(r'^$', views.index),     # This line has changed!
url(r'^new/$', views.new),
url(r'^create/$', views.create),
url(r'^(?P<number>\d+)/$',views.blog_num),
url(r'^edit/(?P<number>\d+)/$',views.blog_edit),
url(r'^(?P<number>\d+)/delete/$', views.blog_delete),


]