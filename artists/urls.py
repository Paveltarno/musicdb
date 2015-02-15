from django.conf.urls import patterns, url
from artists import views

urlpatterns = patterns('',
    url(r'^(?P<artist_id>\d+)/?', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.new, name='new'),
    url(r'^create/$', views.create, name='create'),
)