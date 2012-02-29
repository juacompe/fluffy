from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fluffy.views.home', name='home'),
    # url(r'^fluffy/', include('fluffy.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
