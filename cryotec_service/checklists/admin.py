from django.contrib import admin
from checklists.models import ChecklistAnswer, ChecklistQuestion

admin.site.register(ChecklistAnswer)
admin.site.register(ChecklistQuestion)
