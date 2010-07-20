from django.contrib import admin
from checklists.admin import ChecklistAnswerInline
from actions.models import Checkup, Maintenance, Fix, Report, PAction, Action






class CheckupAdmin(admin.ModelAdmin):
    inlines = [ChecklistAnswerInline]

class MaintenanceAdmin(admin.ModelAdmin):
    inlines = [ChecklistAnswerInline]



admin.site.register(Checkup, CheckupAdmin)
admin.site.register(Maintenance, MaintenanceAdmin)
admin.site.register(Fix)
admin.site.register(Report)









#override of the InlineModelAdmin to support the link in the tabular inline
class LinkedInline(admin.options.InlineModelAdmin):
    template = "linked.html"
    admin_model_path = None

    def __init__(self, *args):
        super(LinkedInline, self).__init__(*args)
        if self.admin_model_path is None:
            self.admin_model_path = "actions/" + self.model.__name__.lower()





class ActionInline(LinkedInline):
    model = Action


class ReportInline(LinkedInline):
    model = Report


class FixInline(LinkedInline):
    model = Fix
    
    
    

class MaintenanceInline(LinkedInline):
    model = Maintenance


class CheckupInline(LinkedInline):
    model = Checkup