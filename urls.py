from django.conf.urls import patterns, include, url
from bookdb.views import*

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mylibrary.views.home', name='home'),
    # url(r'^mylibrary/', include('mylibrary.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    url(r'^library/search/$', 'bookdb.views.search_from'),
    url(r'^library/name_search/$', 'bookdb.views.name_search'),
    url(r'^library/add/$', 'bookdb.views.add'),
    url(r'^library/if_add/$', 'bookdb.views.insert'),
    url(r'^library/back/$', 'bookdb.views.search_from'),
    url(r'^library/detail/$', 'bookdb.views.detail'),
    url(r'^library/update/$', 'bookdb.views.update'),
    url(r'^library/delete/$', 'bookdb.views.delete'),
    url(r'^library/supdate/$', 'bookdb.views.supdate'),
)
