from django.contrib import admin
from files.models import Upload
from libs.admin import LinkedInline

admin.site.register(Upload)


class UploadInline(LinkedInline):
    model = Upload
