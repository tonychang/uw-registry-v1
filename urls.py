from django.conf.urls.defaults import *

urlpatterns = patterns('uwregistry',
    (r'^$', 'views.home'),

    (r'^learn$', 'views.learn'),
    (r'^discover$', 'views.discover'),
    (r'^connect$', 'views.connect'),
                       
    (r'^service/add/$', 'views.submit'),
    (r'^service/browse/$', 'views.browse'),
    (r'^service/mine/$', 'views.mine'),
    (r'^service/next/$', 'views.whatsnext'),
    (r'^service/recent/$', 'views.recent_activity'),                       
    (r'^service/edit/(?P<nick>[-\w]+)/$', 'views.edit'),
    (r'^(?P<nick>[-\w]+)/$', 'views.service'),
)
