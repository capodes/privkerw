from django.conf.urls import patterns, include, url
import Login.views
import Register.views
import Panel.urls
import Application.urls
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'MCC.views.home', name='home'),
    # url(r'^MCC/', include('MCC.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login', Login.views.index),
    url(r'^accounts/register', Register.views.index),
    url(r'^user/panel/', include(Panel.urls)),
    url(r'^user/panel/applications/', include(Application.urls))
    # Examples:
)
