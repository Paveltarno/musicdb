from django.conf.urls import patterns, url
from artists import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<artist_name>\d+)/vote/$', views.add_artist, name='add_artist'),
)