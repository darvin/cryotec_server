from django.contrib import admin
from files.models import Upload
from files.forms import UploadInlineForm
from django.contrib.contenttypes import generic

admin.site.register(Upload)



class UploadInline(generic.GenericStackedInline):
    form = UploadInlineForm
    model = Upload
    


