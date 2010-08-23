# -*- coding: utf-8 -*-
from pprint import pprint

from PyQt4 import QtCore, QtGui, uic  # подключает основные модули PyQt

from models import ReportModel

from actiondialog import *
from Connection import Service


# прототип главной формы
class MainForm(QtGui.QMainWindow):
 
    # конструктор
    def __init__(self):
        super(MainForm, self).__init__()
        
        
        self.service = Service()
 
        # динамически загружает визуальное представление формы
        self.ui = uic.loadUi("mainform.ui", self)
        
        
        self.report_model = ReportModel(self.service, self)
        self.ui.report_table.setModel(self.report_model)
        
        
        
#        self.ui.machines_tree.setColumnHidden(1,True)
#        self.ui.machines_tree.setColumnHidden(2,True)
        
        mlist = self.service.machine_list

        citems = {}

        for machine in mlist:
            citem = self.get_or_create(citems,machine["client"]["name"], \
                                           {"item": \
                                            self.createItem(machine["client"]["name"],\
                                                            machine["client"]["id"], "client"),\
                                            "machinemarks":{}})
            mmitem = self.get_or_create(citem["machinemarks"],machine["machinemark"]["name"], \
                                           {"item": self.createItem(machine["machinemark"]["name"],\
                                                                    machine["machinemark"]["id"], "mark"),\
                                            "machines":{}})
            
            mitem = self.createItem(self.service.get_machine_name_by_id(machine["id"]), machine["id"], "machine")
            self.ui.machines_tree.addTopLevelItem(citem["item"])
            citem["item"].addChild(mmitem["item"])
            mmitem["item"].addChild(mitem)
        
            
        
        self.connect(self.create_report_button,QtCore.SIGNAL("clicked()"),self.createReportDialog)

                
    
    def createReportDialog(self):
        machineid = self.getMachineId()
        if machineid is not None:
            report_dialog = ReportDialog(parent = self)
            report_dialog.setData({("machine", "id"):machineid})
            if report_dialog.exec_() == QtGui.QDialog.Accepted:
                self.report_model.addFromDialog( report_dialog)
        
        
    def getMachineId(self):
        try:
            item = self.ui.machines_tree.selectedItems()[0]
        
            if item.data(1, QtCore.Qt.UserRole) == "machine":
                return item.data(0, QtCore.Qt.UserRole)
        except IndexError:
            pass
        return None
        
    def get_or_create(self, dict, index, data):
        try:
            return dict[index]
        except KeyError:
            dict[index] = []
            dict[index]= data
            return dict[index]
            
    
    def createItem(self, name, id, type):
        item = QtGui.QTreeWidgetItem()
        item.setData(0, QtCore.Qt.DisplayRole, QtCore.QVariant(name))
        item.setData(0, QtCore.Qt.UserRole, QtCore.QVariant(id))
        item.setData(1, QtCore.Qt.UserRole, QtCore.QVariant(type))
        return item