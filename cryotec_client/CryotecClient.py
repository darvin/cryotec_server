# -*- coding: utf-8 -*-

'''
@author: darvin
'''

import pyjd # this is dummy in pyjs

from pyjamas import Window
from pyjamas.ui.DockPanel import DockPanel
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.DisclosurePanel import DisclosurePanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.MenuBar import MenuBar
from pyjamas.ui.MenuItem import MenuItem
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HTML import HTML
from LeftPanel import LeftPanel
from RightPanel import RightPanel


from JsonRpcProxy import jsonrpc_proxy
from Filters import MachineFilter

class CryotecClient(object):
    '''
    classdocs
    '''
        
    def onModuleLoad(self):
        self.singleton = self
        
#        self.selected_client_pk = -1
#        self.selected_machine_pk = -1
#        self.selected_machinetype_pk = -1
#        self.selected_machinemark_pk = -1
#        
        
        self.machine_filter = MachineFilter(-1,-1,-1)
        
        self.leftpanel = LeftPanel(self.singleton)
        leftpanel_outer = DisclosurePanel("Машины")
        leftpanel_outer.add(self.leftpanel)
        
        self.rightpanel = RightPanel(self.singleton)
        
        
        self.menubar = MenuBar(vertical=False)
        
        outer = DockPanel()
        outer.add(self.menubar, DockPanel.NORTH)
        outer.add(leftpanel_outer, DockPanel.WEST)
        outer.add(self.rightpanel, DockPanel.CENTER)
        outer.setWidth("100%")
        outer.setSpacing(12)
        outer.setCellWidth(self.rightpanel, "100%")


        RootPanel().add(outer)
        
        self.init_menubar()
        
        RootPanel().setWidth("100%")

        Window.enableScrolling(False)
        Window.setMargin("2px")
        Window.addWindowResizeListener(self)
        #self.onWindowResized(Window.getClientWidth(), Window.getClientHeight())
        
    
    def call_rpc_actions_getByMachine(self, handler):
        jsonrpc_proxy.actions_getByMachine(self.selected_machine_pk, self.selected_client_pk, self.selected_machinemark_pk, handler)
    
        
    def call_rpc_machines_get(self, handler):
        jsonrpc_proxy.machines_get(self.selected_machine_pk, self.selected_client_pk, self.selected_machinemark_pk, handler)

    def call_rpc_clients_get(self, handler):
        jsonrpc_proxy.clients_get(self.selected_client_pk, handler)


    def init_menubar(self):
        menu1 = MenuBar(vertical=True)
        menu1.addItem("Item 1", MenuCmd(self, "onMenu1Item1"))
        menu1.addItem("Item 2", MenuCmd(self, "onMenu1Item2"))

        menu2 = MenuBar(vertical=True)
        menu2.addItem("Apples", MenuCmd(self, "onMenu2Apples"))
        menu2.addItem("Oranges", MenuCmd(self, "onMenu2Oranges"))

        self.menubar.addItem(MenuItem("Menu 1", menu1))
        self.menubar.addItem(MenuItem("<i>Menu 2</i>", True, menu2))
       

#        
#    def init_rightpanel(self):
#        self.rightpanel.add(HTML("правая панель1"))
#        self.rightpanel.add(HTML("правая панель 2"))


    def onWindowResized(self, width, height):
        # Adjust the shortcut panel and detail area to take up the available room
        # in the window.
        #Logger("Window resized", "width: " + width+ ", height: " + height)

        shortcutHeight = height - self.leftpanel.getAbsoluteTop() - 80
        if (shortcutHeight < 1):
            shortcutHeight = 1
        self.leftpanel.setHeight("%dpx" % shortcutHeight)

        # Give the mail detail widget a chance to resize itself as well.
        self.rightpanel.adjustSize(width, height)




class MenuCmd:
    def __init__(self, object, handler):
        self._object  = object
        self._handler = handler

    def execute(self):
        handler = getattr(self._object, self._handler)
        handler()

        
if __name__=="__main__":
    pyjd.setup("http://127.0.0.1:8000/site_media/client/CryotecClient.html")
    c = CryotecClient()
    c.onModuleLoad()
    pyjd.run()
