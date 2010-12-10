from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
import machines.views
import clients.views
import actions.views
import checklists.views

from django.contrib import admin
admin.autodiscover()

import os

urlpatterns = patterns('',

    url(r'^admin_tools/', include('admin_tools.urls')),
    (r'^admin/doc/(?P<path>.*)$', 'django.views.static.serve', 
         {'document_root':     os.path.join(os.path.dirname(__file__),
                                            'client_doc'),
          'show_indexes':True
          }),
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    #qtdjango api
    (r'^api/', include('qtdjango.django_qtdjango.urls')),

)



urlpatterns += staticfiles_urlpatterns()
