# -*- coding: utf-8 -*-

'''
@author: darvin
'''

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from views import MachineTreeView


class MainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        self.notebook = CentralNotebook()
        self.machine_tree = MachineTreeView()
        self.setCentralWidget(self.notebook)
        
        dockWidget = QDockWidget(u"Оборудование", self)
        dockWidget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        dockWidget.setWidget(self.machine_tree)
        self.addDockWidget(Qt.LeftDockWidgetArea, dockWidget)
        
        self.statusBar()
        

from views import ReportView
class CentralNotebook(QTabWidget):
    note_widgets = {u"Сообщения об ошибках":ReportView}
    def __init__(self, parent=None):
        super(CentralNotebook, self).__init__(parent)
        for label, widget in self.note_widgets.items():
            self.addTab(widget(), label)
        
        


import sys

def main():
    app = QApplication(sys.argv)  # создаёт основной объект программы
    form = MainWindow()  # создаёт объект формы
    form.show()  # даёт команду на отображение объекта формы и содержимого
    app.exec_()  # запускает приложение
 
 
if __name__ == "__main__":
    sys.exit(main()) 