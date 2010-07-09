# -*- coding: utf-8 -*-


'''
@author: darvin
'''


from pyjamas.ui.StackPanel import StackPanel
from pyjamas.ui.Tree import Tree
from pyjamas.ui.ListBox import ListBox
from pyjamas.ui.TreeItem import TreeItem
from pyjamas import DOM, Window
from pyjamas.ui.TabPanel import TabPanel
from pyjamas.ui.HTML import HTML

import Tabs

class RightPanel(TabPanel):
    '''
    classdocs
    '''


    def __init__(self, app):
        '''
        Constructor
        '''
        
        TabPanel.__init__(self, Width="100%", Height="250px")
        self.app = app
        
        self.tabs = []
        for tab_cls in Tabs.TAB_CLASSES:
            tab = tab_cls(self.app)
            
            self.add(tab, tab.get_title(), asHTML=True)
            self.tabs.append(tab)


        self.selectTab(0)
        
        
    def adjustSize(self, windowWidth, windowHeight):
        scrollWidth = windowWidth - self.getAbsoluteLeft() - 9
        if (scrollWidth < 1):
            scrollWidth = 1

        scrollHeight = windowHeight - self.getAbsoluteTop() - 9
        if (scrollHeight < 1):
            scrollHeight = 1

        self.setSize("%d" % scrollWidth, "%d" % scrollHeight)


      
