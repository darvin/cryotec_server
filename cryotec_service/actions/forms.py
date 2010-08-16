# -*- coding: utf-8 -*-


from django.forms import ModelForm, ModelChoiceField, CharField
from actions.models import Report, PAction

class ReportAdminForm(ModelForm):
    paction = ModelChoiceField(PAction.objects.all(), empty_label="Сообщено пользователем")
    
    def __init__(self, *args, **kwargs):
        super(ReportAdminForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        try:
            self.fields['reporttemplate'].queryset = instance.machine.machinemark.reporttemplate_set.all()
        except:

            self.fields['reporttemplate'].widget.attrs['disabled'] = 'disabled'
            #self.fields['reporttemplate'] = CharField()
            
    class Meta:
        model = Report