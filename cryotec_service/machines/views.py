from machines.models import Machine, MachineMark, MachineType
from clients.models import Client
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#from libs import render_to
from jsonrpc import jsonrpc_method

from django.core import serializers
#
#@render_to('machines_tree.html')
#def tree(request):
#    return {}



#@jsonrpc_method('machines.sayHello')
#def whats_the_time(request, name='Lester'):
#    return "Hello %s" % name
#
#@jsonrpc_method('machines.gimmeThat', authenticated=True)
#def something_special(request, secret_data):
#    return {'sauce': ['authenticated', 'sauce']}
#


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
#    print "FUCUUU!!! %s %s %s " % (machine_pk,client_pk, machinemark_pk)
    m = Machine.objects.get_by_machine_client_mark(machine_pk, client_pk, machinemark_pk)
#    m = Machine.objects.filter(pk=machine_pk)
    #m = Machine.objects.get(pk=machine_pk)
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


#
#@jsonrpc_method('machines.getTree()') 
#def getTree():
#    m = Machine.objects.all()
#    mt = {}
#    for machine in m:
#        try:
#            mt[machine.machinemark.machinetype.pk][machine.machinemark.pk] = machine
#        except KeyError:
#            mt[machine.machinemark.machinetype.pk] = {}
#            mt[machine.machinemark.machinetype.pk][machine.machinemark.pk] = machine
#    print mt
#    print "sheet"
#    return serializers.serialize('json', [mt], indent=4)
#    
