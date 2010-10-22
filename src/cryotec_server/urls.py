from django.conf.urls.defaults import *
from django.conf import settings
import machines.views
import clients.views
import actions.views
import checklists.views

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',

    url(r'^admin_tools/', include('admin_tools.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    #qtdjango api
    (r'^api/', include('qtdjango.django_qtdjango.urls')),

 
)
if settings.DEBUG:
    import os
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', 
         {'document_root':     os.path.join(os.path.dirname(__file__), 'media'),
          'show_indexes':True
          }),
    )
