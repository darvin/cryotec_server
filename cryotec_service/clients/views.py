from clients.models import Client
from jsonrpc import jsonrpc_method
from django.core import serializers


@jsonrpc_method('clients_getAll()') 
def getAll(request):
    cs = Client.objects.all()
    return serializers.serialize('json', cs, indent=4)


@jsonrpc_method('clients_get(client_pk=int)') 
def get(request, client_pk):
    if not (client_pk in (None, -1)):
        c = [Client.objects.get(pk=client_pk)]
    else:
        c = Client.objects.all()
    return serializers.serialize('json', c, indent=4)
