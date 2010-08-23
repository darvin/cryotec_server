# -*- coding: utf-8 -*-



from PyQt4 import QtGui, QtCore, Qt

from fieldwidgets import *

class ActionDialog(QtGui.QDialog):
    fields = {}
    
    
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.service = parent.service
        self.setModal(True)
        formLayout = QtGui.QFormLayout()
        
        self.widgets = {}
        
        for fieldname in self.fields:
            fieldopts = self.fields[fieldname]
            self.widgets[fieldname] = fieldopts[1](parent=self)
            formLayout.addRow(fieldopts[0], self.widgets[fieldname])
        
        
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok
                                      | QDialogButtonBox.Cancel)
        
        Qt.QObject.connect(buttonBox, Qt.SIGNAL("accepted()"), self, Qt.SLOT("accept()"));
        Qt.QObject.connect(buttonBox, Qt.SIGNAL("rejected()"), self, Qt.SLOT("reject()"));
        formLayout.addRow(buttonBox)
        self.setLayout(formLayout)
        
    def getData(self):
        res = {}
        
        for fieldname in self.widgets:
            res[fieldname] = self.widgets[fieldname].getData()
        return res
    
    def setData(self, datadict):
        for fieldname in self.widgets:
            try:
                self.widgets[fieldname].setData(datadict[fieldname])
            except KeyError:
                pass

class ReportDialog(ActionDialog):
    fields = {("machine", "id"): (u"Машина", MachineLabel),
              "comment": (u"Комментарий", FieldTextEdit),
#              "reporttemplate":(u"Стандартная неисправость", FieldComboBox),
#              "paction":(u"Техосмотр", FieldComboBox),
#              "level":(u"Уровень неисправности", FieldComboBox),
              
              }
    