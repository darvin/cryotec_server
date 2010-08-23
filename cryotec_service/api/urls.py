from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.emitters import PickleEmitter
from api.handlers import  ReportsHandler, MachinesHandler, ClientsHandler, MachineTypesHandler, MachineMarksHandler

reports_handler = Resource(ReportsHandler)
machines_handler = Resource(MachinesHandler)
machinemarks_handler = Resource(MachineMarksHandler)
machinetypes_handler = Resource(MachineTypesHandler)
clients_handler = Resource(ClientsHandler)

urlpatterns = patterns('',
   url(r'^reports/', reports_handler),
   url(r'^clients/', clients_handler),
   url(r'^machines/', machines_handler),
   url(r'^machinemarks/', machinemarks_handler),
   url(r'^machinetypes/', machinetypes_handler),
   
)