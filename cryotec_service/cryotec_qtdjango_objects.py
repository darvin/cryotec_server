'''
@author: darvin
'''

from cryotec_service.actions.models import Report, Checkup, Fix, Maintenance
from cryotec_service.clients.models import Client
from cryotec_service.machines.models import Machine,MachineMark , MachineType
from cryotec_service.files.models import Upload
from cryotec_service.actiontemplates.models import ReportLevel, ReportTemplate
from cryotec_service.checklists.models import ChecklistAnswer, ChecklistQuestion
try:
    from django.contrib.auth.models import User
except ImportError:
    from qtdjango.models import User

current_module =__import__(__name__)

models = {r"actions/reports/":Report,
          r"actions/checkups/":Checkup,
          r"actions/fixes/":Fix,
          r"actions/maintenances/":Maintenance,
          r"clients/clients/":Client,
          r"machines/machines/":Machine,
          r"machines/machinemarkes/":MachineMark,
          r"machines/machinetypes/":MachineType,
#          r"files/uploads/":Upload,
          r"actiontemplates/reportlevels/":ReportLevel,
          r"actiontemplates/reporttemplates/":ReportTemplate,
          r"checklists/checklistanswers/":ChecklistAnswer,
          r"checklists/checklistquestions/":ChecklistQuestion,
          r"django/users/":User,
          }
          
#
#for model in models:
#    setattr(current_module, model.__name__, model)




if __name__=="__main__":
    print models