# -*- coding: utf-8 -*-


'''
@author: darvin
'''
from django.forms.models import ModelForm, BaseModelFormSet, BaseInlineFormSet
from checklists.models import ChecklistAnswer, ChecklistQuestion




class ChecklistAnswerInlineForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ChecklistAnswerInlineForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        try:
            self.fields['checklistquestion'].queryset = instance.maitenance.machine.machinemark.checklistquestion_set.all()
            self.fields['comment'].required = instance.checklistquestion.required
        except:
            pass
#        if instance and instance.id:

        
#        self.fields['checklistquestion'].widget.attrs['disabled'] = 'disabled'

    
    
    class Meta:
        model = ChecklistAnswer

#    def clean_checklistquestion(self):
#        # As shown in the above answer.
#        instance = getattr(self, 'instance', None)
#        if instance:
#            return instance.checklistquestion
#        else:
#            return self.cleaned_data.get('checklistquestion', None)

    
    
class ChecklistAnswerInlineFormset(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        if kwargs['instance'].id is not None:
            checkquestions = kwargs['instance'].machine.machinemark.checklistquestion_set.all()
    #        print checkquestions
            qs = kwargs['instance'].checklistanswer_set.all()
            for cq in checkquestions:
                try:
                    answer = qs.get(checklistquestion__pk=cq.pk)
                    
                except ChecklistAnswer.DoesNotExist:
                    if cq.required:
                        comment = "введите ответ"
                    else:
                        comment = ""
                    answer = cq.checklistanswer_set.create(maintenance=kwargs['instance'], \
                                                           comment=comment, )
                    answer.save()
                print answer
            
            
            self.queryset = kwargs['instance'].checklistanswer_set.all()
        super(ChecklistAnswerInlineFormset, self).__init__(*args, **kwargs)
