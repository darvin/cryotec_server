from django.contrib import admin
from clients.models import Client, ContactFace
from machines.admin import MachineClientInline,\
    MachineCustomerInline
from files.admin import UploadInline
from libs.admin import LinkedInline



class ContactFaceInline(LinkedInline):
    model = ContactFace


class ClientAdmin(admin.ModelAdmin):
    inlines = [MachineClientInline, MachineCustomerInline, ContactFaceInline]
    inlines += [UploadInline]


    
admin.site.register(Client, ClientAdmin)

