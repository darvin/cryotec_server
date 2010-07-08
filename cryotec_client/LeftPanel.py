# -*- coding: utf-8 -*-


'''
@author: darvin
'''
#from JsonRpcProxy import json_service

from pyjamas.ui.StackPanel import StackPanel
from pyjamas.ui.Tree import Tree
from pyjamas.ui.ListBox import ListBox
from pyjamas.ui.TreeItem import TreeItem
from pyjamas import DOM, Window
from pyjamas.ui.HTML import HTML




from JsonRpcProxy import jsonrpc_proxy




class ClientsListBox(ListBox):
    def __init__(self, app):
        ListBox.__init__(self)  
        self.app = app
        self.addChangeListener(getattr(self, "onItemSelected"))

        
    def refresh(self):
        self.app.selected_client_pk = -1
        self.app.call_rpc_clients_get(self)
        
    def onItemSelected(self, event):
        
        print "selected"
        self.client_pk = self.getValue(self.getSelectedIndex())
        print self.client_pk
        self.app.selected_client_pk = int(self.client_pk) 
        
        self.app.selected_machine_pk = -1
        self.app.selected_machinetype_pk = -1
        self.app.selected_machinemark_pk = -1
        self.app.leftpanel.machines.refresh()
        
    def onRemoteResponse(self, response, request_info):
        self.clear()
        self.addItem(u"Все", "-1")

        response_decoded = jsonrpc_proxy.decode(response)
        for client in response_decoded:
            self.addItem(client["fields"]["name"], str(client["pk"]))


    def onRemoteError(self, code, message, request_info):
        print "error"
        print ("error %s" % str(message))


class MachinesTree(Tree):
    def __init__(self, app):
        Tree.__init__(self)
        self.app = app
        self.addTreeListener(self)
        
    def refresh(self):
        self.app.call_rpc_machines_get(self)
#        print "machines refresh %s" % client_pk
 

    def onTreeItemSelected(self, item):
        value = item.getUserObject()
        
        if value is not None:
            print value
            t, v = value.split(";")
            if t == "machine":
                self.app.selected_machine_pk = int(v)
            elif t=="machinemark":
                self.app.selected_machine_pk = -1
                self.app.selected_machinemark_pk = int(v)
            elif (t=="all") and (v==1):
                self.app.selected_machine_pk = -1
                

            
            self.app.rightpanel.refresh()


    def onTreeItemStateChanged(self, item):
        pass # We ignore this.


    def onRemoteResponse(self, response, request_info):
        response_decoded = jsonrpc_proxy.decode(response)
        
        self.clear()
        self.addItem(self.createItem(u"Все", value="all;%s"%str(-1)))
        
        def process_mark(mark, marks, machineitem, types, type, mark_name):
            if mark in marks:
                marks[mark].addItem(machineitem)
            else:
                markitem = self.createItem(mark_name,value="machinemark;%s"%mark)
                marks[mark] = markitem
                marks[mark].addItem(machineitem)
                types[type].addItem(markitem)
        
        marks = {}
        types = {}
        
        print response_decoded
        for machine in response_decoded:
            machineitem = self.createItem(machine["extras"]["__unicode__"],value="machine;%s"%machine["pk"])
            type = machine["extras"]["get_machinetype_pk"]
            mark = machine["extras"]["get_machinemark_pk"]
            type_name = machine["extras"]["get_machinetype_name"]
            mark_name = machine["extras"]["get_machinemark_name"]
            if type in types:
                process_mark(mark, marks, machineitem, types, type, mark_name)
            else:
                typeitem = self.createItem(type_name,value="machinetype;%s"%type)
                types[type] = typeitem
                self.addItem(typeitem)
                process_mark(mark, marks, machineitem, types, type, mark_name)
#    def onRemoteResponse(self, response, request_info):
#        def get_or_create(dic, ind1, ind2):
#            if ind1 in dic:
#                if ind2 in dic[ind1]:
#                    return dic[ind1][ind2]
#                else:
#                    dic[ind1][ind2] = []
#                    return dic[ind1][ind2]
#            else:
#                dic[ind1] = {}
#                dic[ind1][ind2] = []
#                return dic[ind1][ind2]
#             
#        response_decoded = jsonrpc_proxy.decode(response)
#        machines = {}
#        for machine in response_decoded:
##            print machine
#            type = machine["extras"]["get_machinetype_name"]
#            mark = machine["extras"]["get_machinemark_name"]
#            
#            get_or_create(machines,type,mark).append({"name": machine["extras"]["__unicode__"],
#                                         "pk": machine["pk"]})
#            
#        self.clear()
#        self.addItem(self.createItem(u"Все", value="all;%s"%str(-1)))
#        for type in machines:
#            typeitem = self.createItem(type)
#            self.addItem(typeitem)
#            for mark in machines[type]:
#                markitem = self.createItem(mark)
#                typeitem.addItem(markitem)
#                for machine in machines[type][mark]:
#                    print machine
#                    machineitem = self.createItem(machine["name"],value="machine;%s"%machine["pk"])
#                    markitem.addItem(machineitem)

    def onRemoteError(self, code, message, request_info):
        print "error"
        print ("error %s" % str(message))
        
    
    

    def createItem(self, label, value=None):
        item = TreeItem(HTML(label))
        DOM.setStyleAttribute(item.getElement(), "cursor", "pointer")
        if value is not None:
            item.setUserObject(value)
        return item
    
class LeftPanel(StackPanel):
    '''
    classdocs
    '''


    def __init__(self, app):
        '''
        Constructor
        '''
        StackPanel.__init__(self)
        self.app = app
        
        self.machines = MachinesTree(self.app)
        self.clients = ClientsListBox(self.app)
        self.clients.setVisibleItemCount(13)
        
       
        self.add(self.machines, "Машины")
        self.add(self.clients, "Клиенты")
        
        self.machines.refresh()
        self.clients.refresh()
        self.clients.selectValue("-1")

