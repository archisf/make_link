from django.conf.urls import patterns, include, url


urlpatterns = patterns('alice_links.views',
                       url(r'^(?P<short_id>\w{6})$', 'redirect_original', name='redirectoriginal'),
                       url(r'^shortlink/$', 'add_shorten_url', name='add_shorten_url'),
                       url(r'^$', 'latest_urls', name='latest_urls'),
                       )


