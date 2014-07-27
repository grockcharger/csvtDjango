from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'csvt10.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^regist/$','online.views.regist'),
    url(r'^login/$','online.views.login'),
    url(r'^index/$','online.views.index'),
    url(r'^logout/$','online.views.logout'),
)
