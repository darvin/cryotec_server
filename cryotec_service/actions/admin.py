from django.contrib import admin
from actions.models import Checkup, Maintenance, Fix, Report, PAction

admin.site.register(Checkup)
admin.site.register(Maintenance)
admin.site.register(Fix)
admin.site.register(Report)
