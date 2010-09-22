
        

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
    