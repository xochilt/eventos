from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls import include, url


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'web.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^blog/$', 'web.views.blog', name='blog'),
    url(r'^about/$', 'web.views.about', name='about'),
    url(r'^contact/$', 'web.views.contact', name='contact'),
     url('^payments/', include('payments.urls'))
    #url(r'^admin/', include(admin.site.urls)),
)
