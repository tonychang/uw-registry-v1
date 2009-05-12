from django.conf.urls.defaults import *

urlpatterns = patterns('uwregistry',
    (r'^$', 'views.home'),
    (r'^service/add/$', 'views.submit'),
    (r'^service/browse/$', 'views.browse'),
    (r'^service/mine/$', 'views.mine'),
    (r'^service/edit/(?P<nick>[-\w]+)/$', 'views.edit'),
    (r'^(?P<nick>[-\w]+)/$', 'views.service'),
)
