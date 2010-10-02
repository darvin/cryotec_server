# -*- coding: utf-8 -*-

from piston.handler import BaseHandler
from actions.models import Report, Action
from machines.models import Machine, MachineMark, MachineType
from clients.models import Client
from actiontemplates.models import ReportLevel, ReportTemplate


class CollectionHandler(BaseHandler):
    exclude = ()
    allowed_methods = ('GET',)
    
    def read(self, request,  *args, **kwargs):
        filterargs = {}
        for arg in request.GET:
            filterargs[arg] = request.GET[arg]

        return self.model.objects.filter(**filterargs) 

class ReportsHandler(CollectionHandler):
    model = Report
#    fields = ("id","comment", "date", "interest", ("reporttemplate", ("id", "comment", "interest")),\
#              \
#              ("machine",("id","name",("client", ("name", "id",)) ,("machinemark",("name","id",))) ) )
#
#
# 


class MachinesHandler(CollectionHandler):
    model = Machine

class MachineMarksHandler(CollectionHandler):
    model = MachineMark 
 
 
 
class MachineTypesHandler(CollectionHandler):
    model = MachineType 



class ClientsHandler(CollectionHandler):
    model = Client 
    
    
class ReportLevelsHandler(CollectionHandler):
    model = ReportLevel
    
class ReportTemplatesHandler(CollectionHandler):
    model = ReportTemplate
    





