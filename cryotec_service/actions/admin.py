from django.contrib import admin
from checklists.admin import ChecklistAnswerInline
from actions.models import Checkup, Maintenance, Fix, Report, PAction, Action

from libs.admin import LinkedInline




class CheckupAdmin(admin.ModelAdmin):
    inlines = [ChecklistAnswerInline]

class MaintenanceAdmin(admin.ModelAdmin):
    inlines = [ChecklistAnswerInline]



admin.site.register(Checkup, CheckupAdmin)
admin.site.register(Maintenance, MaintenanceAdmin)
admin.site.register(Fix)
admin.site.register(Report)











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