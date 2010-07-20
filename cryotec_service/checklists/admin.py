from django.contrib import admin
from checklists.models import ChecklistAnswer, ChecklistQuestion

admin.site.register(ChecklistAnswer)
admin.site.register(ChecklistQuestion)



class ChecklistAnswerInline(admin.TabularInline):
    model = ChecklistAnswer


class ChecklistQuestionInline(admin.TabularInline):
    model = ChecklistQuestion