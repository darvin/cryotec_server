from django.contrib import admin
from actions.admin import FixInline, ReportInline, MaintenanceInline, CheckupInline
from checklists.admin import ChecklistQuestionInline
from machines.models import Machine, MachineMark, MachineType






class MachineInline(admin.TabularInline):
    model = Machine

class MachineMarkInline(admin.TabularInline):
    model = MachineMark


class MachineMarkAdmin(admin.ModelAdmin):
    inlines = [ChecklistQuestionInline, MachineInline]

class MachineTypeAdmin(admin.ModelAdmin):
    inlines = [MachineMarkInline]

class MachineAdmin(admin.ModelAdmin):
    inlines = [ReportInline, FixInline, MaintenanceInline, CheckupInline]



admin.site.register(Machine, MachineAdmin)
admin.site.register(MachineMark, MachineMarkAdmin)
admin.site.register(MachineType, MachineTypeAdmin)

