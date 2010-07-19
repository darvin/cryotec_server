from django.contrib import admin
from actions.models import Checkup, Maintenance, Fix, Report, PAction, Action

admin.site.register(Checkup)
admin.site.register(Maintenance)
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





class ActionInline(admin.StackedInline):
    model = Action


class ReportInline(admin.StackedInline):
    model = Report


class FixInline(LinkedInline):
    model = Fix
    
    
    

class MaintenanceInline(LinkedInline):
    model = Maintenance


class CheckupInline(LinkedInline):
    model = Checkup