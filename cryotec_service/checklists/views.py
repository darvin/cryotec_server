from checklists.models import ChecklistAnswer, ChecklistQuestion
from jsonrpc import jsonrpc_method
from django.core import serializers


@jsonrpc_method('checklists_getAllQ()') 
def getAllQ(request):
    cs = ChecklistQuestion.objects.all()
    return serializers.serialize('json', cs, indent=4)


@jsonrpc_method('checklists_getQ(checklist_q_pk=int)') 
def getQ(request, checklist_q_pk):
    c = ChecklistQuestion.objects.get(pk=checklist_q_pk)
    return serializers.serialize('json', [c], indent=4)




@jsonrpc_method('checklists_getAllA()') 
def getAllA(request):
    cs = ChecklistAnswer.objects.all()
    return serializers.serialize('json', cs, indent=4)


@jsonrpc_method('checklists_getA(checklist_a_pk=int)') 
def getA(request, checklist_a_pk):
    c = ChecklistAnswer.objects.get(pk=checklist_a_pk)
    return serializers.serialize('json', [c], indent=4)
