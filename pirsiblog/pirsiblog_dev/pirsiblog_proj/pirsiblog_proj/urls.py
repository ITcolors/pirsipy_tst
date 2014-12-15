from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pirsiblog_proj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name = 'index.html')),
    url(r'^posting/', include('posting.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
