from django.contrib import admin
from clients.models import Client
from machines.admin import MachineInline


class ClientAdmin(admin.ModelAdmin):
    inlines = [MachineInline]
    
admin.site.register(Client, ClientAdmin)

