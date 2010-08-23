from PyQt4.QtGui import *
from PyQt4 import QtCore


class FieldWidget(object):
    def __init__(self, parent):
        self.service = parent.service

        
    def getData(self):
        raise NotImplementedError
    
    def setData(self, data):
        raise NotImplementedError

class FieldLabel(QLabel, FieldWidget):
    def __init__(self, parent):
        FieldWidget.__init__(self, parent)
        QLabel.__init__(self, parent)
        
    def getData(self):
        return self.text()
    
    def setData(self, data):
        if data is not None:
            self.setText(data)
        
        
        
        
class FieldTextEdit(QTextEdit, FieldWidget):
    def __init__(self, parent):
        FieldWidget.__init__(self, parent)
        QTextEdit.__init__(self, parent)
        
    def getData(self):
        return self.toPlainText()
    
    def setData(self, data):
        self.setPlainText(QtCore.QString(data))
        
        

class NameByIdFieldLabel(FieldLabel):
    
    
    def __init__(self, parent):
        super(NameByIdFieldLabel, self).__init__(parent)
        self._data = None
    
    def getData(self):
        return self._data
    
    def setData(self, data):
        self._data = data.toInt()[0]
        super(NameByIdFieldLabel, self).setData(self.getNameById())
    
    def getNameById(self):
        raise NotImplementedError

        
        
class MachineLabel(NameByIdFieldLabel):
    
    def getNameById(self):
        return self.service.get_machine_name_by_id(self._data) 
    