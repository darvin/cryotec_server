# -*- coding: UTF-8 -*-

from qtdjango.views import *
from models import *

class MachineView(DetailView):
#    fields = ["comment", "name", "id"]
    pass  
    

class MachinesTableView(TableView):
#    fields = ["alias","serial"]
    model = Machine
 

class MachineTreeView(TableView):
    model = Machine

def main():
    
    
    
#    Machine.load()

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
#    Client.load()
   
##    print Machine.get(3).machinemark.name
#    pprint (Machine.filter(machinemark__id=1))
#    print Machine.filter(machinemark__id=1)[0]
    
    

    
    app = QApplication(sys.argv)  # создаёт основной объект программы
#    form = MachineView(Machine.get(1)) # создаёт объект формы
#    form.show()  # даёт команду на отображение объекта формы и содержимого
    
    form = QMainWindow()
    form.layout().addWidget(MachinesTableView())
    form.show()
    
    
    app.exec_()  # запускает приложение
 
 
if __name__ == "__main__":
    import sys
    sys.exit(main())