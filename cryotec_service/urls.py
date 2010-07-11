from django.conf.urls.defaults import *
from django.conf import settings
from jsonrpc import jsonrpc_site
import machines.views
import clients.views
import actions.views
import checklists.views

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Example:
    # (r'^cryotec_service/', include('cryotec_service.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
    
    url(r'^admin_tools/', include('admin_tools.urls')),
    
    (r'^admin/', include(admin.site.urls)),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),


    url(r'^json/browse/', 'jsonrpc.views.browse', name="jsonrpc_browser"), # for the graphical browser/web console only, omissible
    url(r'^json/', jsonrpc_site.dispatch, name="jsonrpc_mountpoint"),
    (r'^json/(?P<method>[a-zA-Z0-9.]+)$', jsonrpc_site.dispatch), # for HTTP GET only, also omissible


 
)

    
if settings.DEBUG:
    import os
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', 
         {'document_root':     os.path.join(os.path.dirname(__file__), 'media'),
          'show_indexes':True
          }),
    )