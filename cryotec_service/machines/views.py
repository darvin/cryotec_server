from machines.models import Machine, MachineMark, MachineType
from clients.models import Client
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from jsonrpc import jsonrpc_method

from django.core import serializers


@jsonrpc_method('machines_getByClient(client_pk=int)')
def getByClient(request, client_pk=None):
    if client_pk:
        c = Client.objects.get(pk=client_pk)
        m = c.machine_set.all()
    else:
        m = Machine.objects.all()
    return serializers.serialize('json', m, indent=4, extras=('__unicode__','get_absolute_url',
                            'get_machinemark_name', 'get_machinetype_name',
                                                              ))
#                                 relations=('machinemark', 'client', 'machinetype'))

        
@jsonrpc_method('machines_getAll()') #, authenticated=True) 
def getAll(request):
    return getByClient(request, None)




@jsonrpc_method('machines_get(machine_pk=int, client_pk=int, machinemark_pk=int)') 
def get(request, machine_pk=None, client_pk=None, machinemark_pk=None):
    m = Machine.objects.get_by_machine_client_mark(machine_pk, client_pk, machinemark_pk)

    print m
    return serializers.serialize('json', m, indent=4, extras=('__unicode__','get_absolute_url',
                            'get_machinemark_name', 'get_machinetype_name',
                            'get_machinemark_pk', 'get_machinetype_pk',
                                                              ))

@jsonrpc_method('machines_getType(type_pk=int)') 
def getType(request, type_pk):
    m = MachineType.objects.get(pk=type_pk)
    return serializers.serialize('json', [m], indent=4)

@jsonrpc_method('machines_getMark(mark_pk=int)') 
def getMark(request, mark_pk):
    m = MachineMark.objects.get(pk=mark_pk)
    return serializers.serialize('json', [m], indent=4)

