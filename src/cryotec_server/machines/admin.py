# -*- coding: utf-8 -*-


from django.contrib import admin
from actions.admin import FixInline, ReportInline, MaintenanceInline, CheckupInline

from actiontemplates.admin import ReportTemplateInline
from machines.models import Machine, MachineMark, MachineType
from libs.admin import LinkedInline
from files.admin import UploadInline





class MachineClientInline(LinkedInline):
    model = Machine
    fk_name = 'client'
    verbose_name = u"Оборудование, эксплуатируемое клиентом"
    verbose_name_plural = u"Оборудование, эксплуатируемое клиентом"
    
class MachineCustomerInline(LinkedInline):
    model = Machine
    fk_name = 'client'
    verbose_name = u"Оборудование, купленное клиентом"
    verbose_name_plural = u"Оборудование, купленное клиентом"

    
class MachineInline(LinkedInline):
    model = Machine


class MachineMarkInline(LinkedInline):
    model = MachineMark


class MachineMarkAdmin(admin.ModelAdmin):
    inlines = [ReportTemplateInline, MachineInline]
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
    readonly_fields = ["get_current_motohours","get_last_checkup_date"]



admin.site.register(Machine, MachineAdmin)
admin.site.register(MachineMark, MachineMarkAdmin)
admin.site.register(MachineType, MachineTypeAdmin)

