from django.contrib import admin
from checklists.models import ChecklistAnswer, ChecklistQuestion
from libs.admin import LinkedInline
from checklists.forms import ChecklistAnswerInlineForm, ChecklistAnswerInlineFormset


#admin.site.register(ChecklistAnswer)
admin.site.register(ChecklistQuestion)



class ChecklistAnswerInline(LinkedInline):
    model = ChecklistAnswer
    form = ChecklistAnswerInlineForm
    formset = ChecklistAnswerInlineFormset

class ChecklistQuestionInline(LinkedInline):
    model = ChecklistQuestion