'''
@author: darvin
'''

import actions.models
import clients.models
import machines.models
import files.models
import actiontemplates.models
import checklists.models
try:
    from django.contrib.auth.models import User
except ImportError:
    from qtdjango.models import User

current_module =__import__(__name__)

models = {r"actions/reports/":actions.models.Report,
          r"actions/checkups/":actions.models.Checkup,
          r"actions/fixes/":actions.models.Fix,
          r"actions/maintenances/":actions.models.Maintenance,
          r"clients/clients/":clients.models.Client,
          r"machines/machines/":machines.models.Machine,
          r"machines/machinemarkes/":machines.models.MachineMark,
          r"machines/machinetypes/":machines.models.MachineType,
#          r"files/uploads/":Upload,
          r"actiontemplates/reportlevels/":actiontemplates.models.ReportLevel,
          r"actiontemplates/reporttemplates/":actiontemplates.models.ReportTemplate,
          r"checklists/checklistanswers/":checklists.models.ChecklistAnswer,
          r"checklists/checklistquestions/":checklists.models.ChecklistQuestion,
          r"django/users/":User,
          }

for url, model in models.items():
    setattr(current_module, model.__name__, model)




if __name__=="__main__":
    dir(current_module)
