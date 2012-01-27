from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('solidstate.websites.views',
    url(r'^$', 'home'),
)
