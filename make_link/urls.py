from django.conf.urls import patterns, include, url
from django.contrib.auth import views


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'', include('alice_links.urls', namespace='alice_links')),
                       url(r'^model/', include('alice_links.urls', namespace='model')),
                       url(r'^accounts/login/$', views.login, name='login'),
                       url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
                       )
