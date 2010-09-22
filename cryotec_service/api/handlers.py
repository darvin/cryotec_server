# -*- coding: utf-8 -*-

from piston.handler import BaseHandler
from actions.models import Report, Action
from machines.models import Machine, MachineMark, MachineType
from clients.models import Client
from actiontemplates.models import ReportLevel, ReportTemplate
from piston.utils import rc

class CollectionHandler(BaseHandler):
    allowed_methods = ('GET',)
    
    def read(self, request,  *args, **kwargs):
        filterargs = {}
        for arg in request.GET:
            filterargs[arg] = request.GET[arg]

        return self.model.objects.filter(**filterargs) 

class ReportsHandler(CollectionHandler):
    model = Report
    fields = ("id","comment", "date", "interest", ("reporttemplate", ("id", "comment", "interest")),\
              \
              ("machine",("id","name",("client", ("name", "id",)) ,("machinemark",("name","id",))) ) )


 


class MachinesHandler(CollectionHandler):
    model = Machine 
    fields = ("id",("client", ("name", "id",)),("machinemark",("name","id",)),"serial", "alias")


class MachineMarksHandler(CollectionHandler):
    model = MachineMark 
    fields = ("id","machinetype", "name")
 
 
 
class MachineTypesHandler(CollectionHandler):
    model = MachineType 
    fields = ("id", "name")



class ClientsHandler(CollectionHandler):
    model = Client 
    fields = ("id","comment", "name")
    
    
class ReportLevelsHandler(CollectionHandler):
    model = ReportLevel
    
class ReportTemplatesHandler(CollectionHandler):
    model = ReportTemplate
    





