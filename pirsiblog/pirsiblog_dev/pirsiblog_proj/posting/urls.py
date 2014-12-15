from django.conf.urls import patterns, include, url
from posting.views import Index, Details

urlpatterns = patterns('',
    url(r'^$', Index.as_view()),
    url(r'^(?P<id>\d+)/$', Details.as_view())
)