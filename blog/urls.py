from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('solidstate.blog.views',
    url(r'^$', 'home'),
)
