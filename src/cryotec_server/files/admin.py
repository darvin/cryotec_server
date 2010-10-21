from django.contrib import admin
from files.models import Upload
from files.forms import UploadInlineForm
from libs.admin import LinkedInline

admin.site.register(Upload)


class UploadInline(LinkedInline):
    form = UploadInlineForm
    model = Upload
    


