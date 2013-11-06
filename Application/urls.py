from django.conf.urls import patterns, url
import Alexa.views

urlpatterns = patterns('',
                       url(r'alexa', Alexa.views.index)
)