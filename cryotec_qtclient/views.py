# -*- coding: UTF-8 -*-

from qtdjango.views import *
from models import *

class MachineView(DetailView):
#    fields = ["comment", "name", "id"]
    pass  
    

class MachinesTableView(TableView):
#    fields = ["alias","serial"]
    model = Machine
 

class MachineTreeView(TableView):
    model = Machine
    

class ReportView(TableView):
    model = Report
    
#
#class FixView(TableView):
#    model = Fix
#
#
#class MaitenanceView(TableView):
#    model = Maitenance
#    
#
#class CheckupView(TableView):
#    model = Checkup