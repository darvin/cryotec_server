from django.contrib import admin
from checklists.models import ChecklistAnswer, ChecklistQuestion
from libs.admin import LinkedInline

admin.site.register(ChecklistAnswer)
admin.site.register(ChecklistQuestion)



class ChecklistAnswerInline(LinkedInline):
    model = ChecklistAnswer


class ChecklistQuestionInline(LinkedInline):
    model = ChecklistQuestion