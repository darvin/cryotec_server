'''
Created on 07.08.2010

@author: klimov
'''
from files.models import Upload
from django.forms.models import ModelForm

class UploadInlineForm(ModelForm):
    class Meta:
        model = Upload
        fields =("file", )
