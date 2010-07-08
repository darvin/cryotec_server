from actions.models import Action
from jsonrpc import jsonrpc_method
from django.core import serializers


@jsonrpc_method('actions_getAll()') 
def getAll(request):
    cs = Action.objects.all()
    return serializers.serialize('json', cs, indent=4)


@jsonrpc_method('actions_get(action_pk=int)') 
def get(request, action_pk):
    c = Action.objects.get(pk=action_pk)
    return serializers.serialize('json', [c], indent=4)
