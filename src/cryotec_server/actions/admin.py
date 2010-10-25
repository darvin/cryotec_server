from django.contrib import admin
from checklists.admin import ChecklistAnswerInline
from actions.models import Checkup, Maintenance, Fix, Report
from actions.forms import ReportAdminForm
from libs.admin import LinkedInline
from files.admin import UploadInline


class ReportAdmin(admin.ModelAdmin):
    form = ReportAdminForm
    inlines = [UploadInline]
    
    
class FixAdmin(admin.ModelAdmin):
    inlines = [UploadInline]
    
class CheckupAdmin(admin.ModelAdmin):
    inlines = [UploadInline]

class MaintenanceAdmin(admin.ModelAdmin):
    inlines = [ChecklistAnswerInline,UploadInline]



admin.site.register(Checkup, CheckupAdmin)
admin.site.register(Maintenance, MaintenanceAdmin)
admin.site.register(Fix)
admin.site.register(Report, ReportAdmin)







#
#class ActionInline(LinkedInline):
#    model = Action


class ReportInline(LinkedInline):
    model = Report
    form = ReportAdminForm





class FixInline(LinkedInline):
    model = Fix
    
    
    

class MaintenanceInline(LinkedInline):
    model = Maintenance


class CheckupInline(LinkedInline):
    model = Checkup