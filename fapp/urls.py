from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fapp.views.home', name='home'),
    # url(r'^fapp/', include('fapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^login/$', 'blog.views.login_user'),
    url(r'^register/$', 'blog.views.register_user'),
    url(r'^posts/$', 'blog.views.posts_user'),

    url(r'^$', 'blog.views.index'),
    # url(r'^blog/(?P<blog_id>\d+)/$', 'blog.views.detail'),
    # url(r'^blog/(?P<blog_id>\d+)/results/$', 'polls.views.results'),
    # url(r'^blog/(?P<blog_id>\d+)/vote/$', 'polls.views.vote'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)
