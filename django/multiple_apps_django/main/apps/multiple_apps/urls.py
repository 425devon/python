from django.conf.urls import url
from . import views           
urlpatterns = [
url(r'^$', views.index),
url(r'^blogs', views.blogs),
url(r'^blogs/new', views.new_blog),
url(r'^create/$', views.create),
url(r'^(?P<number>\d+)/$',views.blog_num),
url(r'^edit/(?P<number>\d+)/$',views.blog_edit),
url(r'^(?P<number>\d+)/delete/$', views.blog_delete),
]