#!/usr/bin/env python


from PyQt4.QtCore import *

def joinl(data):
#    if isinstance(data,list) or isinstance(data,tuple):
#        return "_".join(data)
#    else:
    return data
        


class ReportModel(QAbstractTableModel):


    fieldnames = (("machine", "id"), "comment", "interest", "date")
    headers = fieldnames
    
    
    def addFromDialog(self, dialog):
        newrow = dialog.getData()
        newrow["date"] = ""
        self.addData(newrow)
        
        
        
    def addData(self, datadict):
        self._data.append(datadict)
        from pprint import pprint
        pprint( self._data)
        self.emit(SIGNAL("dataChanged"))
        
    
    
    def __init__(self, service, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        
        datain = service.get_reports()
        
        
        def ind(dict, index):
            try:
                return dict[index]
            except KeyError:
                print index
                return dict[index[0]][index[1]]
        
  
        self._data = []
        for row in datain:
            dict = {}
            for fieldname in self.fieldnames:
                dict[joinl(fieldname)] = ind(row, fieldname)
            self._data.append(dict)
                
      

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return len(self.headers)

    def data(self, index, role):
       
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self._data[index.row()][joinl(self.fieldnames[index.column()])])

    