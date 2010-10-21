from django.contrib import admin

from actiontemplates.models import ReportTemplate, ReportLevel

from libs.admin import LinkedInline


admin.site.register(ReportTemplate)
admin.site.register(ReportLevel)

class ReportTemplateInline(LinkedInline):
    model = ReportTemplate

