from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect


urlpatterns = patterns('',
    url(r'^$', lambda r: HttpResponseRedirect('artists/')),
    url(r'^artists/', include('artists.urls', namespace="artists"))
)
