from django.contrib import admin
from clients.models import Client
from machines.admin import MachineClientInline,\
    MachineCustomerInline
from files.admin import UploadInline


class ClientAdmin(admin.ModelAdmin):
    inlines = [MachineClientInline, MachineCustomerInline]
    inlines += [UploadInline]


    
admin.site.register(Client, ClientAdmin)

