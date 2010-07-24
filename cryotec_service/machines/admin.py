from django.contrib import admin
from actions.admin import FixInline, ReportInline, MaintenanceInline, CheckupInline
from checklists.admin import ChecklistQuestionInline
from machines.models import Machine, MachineMark, MachineType
from libs.admin import LinkedInline
from files.admin import UploadInline





class MachineClientInline(LinkedInline):
    model = Machine
    fk_name = 'client'
    
class MachineCustomerInline(LinkedInline):
    model = Machine
    fk_name = 'client'
    
class MachineInline(LinkedInline):
    model = Machine


class MachineMarkInline(LinkedInline):
    model = MachineMark


class MachineMarkAdmin(admin.ModelAdmin):
    inlines = [ChecklistQuestionInline, MachineInline]
    inlines += [UploadInline]

class MachineTypeAdmin(admin.ModelAdmin):
    inlines = [MachineMarkInline]

class MachineAdmin(admin.ModelAdmin):
    inlines = [ReportInline, \
               FixInline, \
               MaintenanceInline, \
               CheckupInline, \
               UploadInline, \
               ]



admin.site.register(Machine, MachineAdmin)
admin.site.register(MachineMark, MachineMarkAdmin)
admin.site.register(MachineType, MachineTypeAdmin)

