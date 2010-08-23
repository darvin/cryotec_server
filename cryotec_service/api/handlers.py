from piston.handler import BaseHandler
from actions.models import Report, Action
from machines.models import Machine, MachineMark, MachineType
from clients.models import Client



class CollectionHandler(BaseHandler):
    allowed_methods = ('GET',)
    
    def read(self, request):
       return self.model.objects.all()     

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
 
 
 
class MachineTypesHandler(CollectionHandler):
   model = MachineType 
   



class ClientsHandler(CollectionHandler):
   model = Client 


