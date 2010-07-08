from django.contrib import admin
from machines.models import Machine, MachineMark, MachineType



class MachineInline(admin.StackedInline):
    model = Machine

class MachineMarkInline(admin.StackedInline):
    model = MachineMark


class MachineMarkAdmin(admin.ModelAdmin):
    inlines = [MachineInline]

class MachineTypeAdmin(admin.ModelAdmin):
    inlines = [MachineMarkInline]


admin.site.register(Machine)
admin.site.register(MachineMark, MachineMarkAdmin)
admin.site.register(MachineType, MachineTypeAdmin)

