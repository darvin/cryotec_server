# -*- coding: UTF-8 -*-

'''

@author: darvin
'''
from qtdjango.models import *

    
class MachineType(Model):
    resource_name = "machinetypes"
    
    fields = {"name":CharField()}

    
    def __unicode__(self):
        return self.name

class MachineMark(Model):
    resource_name = "machinemarks"
    
    fields = {"name":CharField(),
              "machinetype":ForeignKey(model=MachineType),
             }
    
    
    def __unicode__(self):
        return self.name

    
class Client(Model):
    resource_name = "clients"
    
    fields = {"name":CharField(),
              "comment":TextField()
            }
    
    def __unicode__(self):
        return self.name

class Machine(Model):
    resource_name = "machines"
    fields = {
              "alias":CharField("Альяс"),
              "serial":CharField("Серийный номер"),
              "client":ForeignKey("Клиент", model=Client),
              "machinemark":ForeignKey("Марка машины", model=MachineMark),}

    
    def __unicode__(self):
        if self.alias is not None:
            return self.alias
        return "%s_%s" % self.client, self.machinemark.name


if __name__=="__main__":
    
    Machine.load()
    from pprint import pprint
#    pprint (MachineModel.objects)
#    pprint (Machine.filter())
#    
#    
##    some = Machine.new()
##    some.save()
#    
##    
#    pprint (Machine.filter())
#    pprint (Machine.get(2))

    Client.load()
#    pprint(Client.get(1).machine_se)
    pprint (Machine.get(1).client)
    pprint (Client.get(1).__dict__)
##    print Machine.get(3).machinemark.name
#    pprint (Machine.filter(machinemark__id=1))
#    print Machine.filter(machinemark__id=1)[0]
    
