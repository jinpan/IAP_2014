from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'IAP_2014.views.home', name='home'),
    url(r'^client/$', 'IAP_2014.views.spiffyClientSide', name='spiffyClientSide'),
    #url(r'^externship/(?P<id>\d{4})/$', 'IAP_2014.views.externship',
    #    name='externship'),
    # url(r'^IAP_2014/', include('IAP_2014.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
