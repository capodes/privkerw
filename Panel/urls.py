from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
                       url(r'index/', index),
                       url(r'logout/', logout),
                       url(r'profile/', profile))