from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.emitters import PickleEmitter
from api.handlers import  ReportsHandler, ReportLevelsHandler, ReportTemplatesHandler, \
        MachinesHandler, ClientsHandler, MachineTypesHandler, MachineMarksHandler

reports_handler = Resource(ReportsHandler)
machines_handler = Resource(MachinesHandler)
machinemarks_handler = Resource(MachineMarksHandler)
machinetypes_handler = Resource(MachineTypesHandler)
clients_handler = Resource(ClientsHandler)
reportlevels_handler = Resource(ReportLevelsHandler)
reporttemplates_handler = Resource(ReportTemplatesHandler)

urlpatterns = patterns('',
   url(r'^reports/', reports_handler),
   url(r'^clients/', clients_handler),
   url(r'^machines/', machines_handler),
   url(r'^machinemarks/', machinemarks_handler),
   url(r'^machinetypes/', machinetypes_handler),
   url(r'^reporttemplates/', reporttemplates_handler),
   url(r'^reportlevels/', reportlevels_handler),
   
)