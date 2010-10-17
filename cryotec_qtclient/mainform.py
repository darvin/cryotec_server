# -*- coding: utf-8 -*-

'''
@author: darvin
'''

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from views import FixWithButtonsView, ReportWithButtonsView, \
        MaintenanceWithButtonsView, CheckupWithButtonsView, MachineTreeView
from qtdjango.models import Model

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.machine_tree = MachineTreeView()
        #self.machine_tree.setSelectionMode(QAbstractItemView.MultiSelection)
        self.notebook = CentralNotebook(self.machine_tree)

        self.setCentralWidget(self.notebook)

        dockWidget = QDockWidget(u"Оборудование", self)

        dockWidget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        dockWidget.setWidget(self.machine_tree)
        self.addDockWidget(Qt.LeftDockWidgetArea, dockWidget)

        self.statusBar()


class CentralNotebook(QTabWidget):
    note_widgets = {
        u"Сообщения об ошибках":ReportWithButtonsView,
        u"Ремонты":FixWithButtonsView,
        u"Техобслуживания":MaintenanceWithButtonsView,
        u"Контроли моточасов":CheckupWithButtonsView,
    }
    def __init__(self, machine_tree, parent=None):
        super(CentralNotebook, self).__init__(parent)
        self.widgets = []
        self.machine_tree = machine_tree
        for label, widget in self.note_widgets.items():
            w = widget()
            machine_tree.modelSelectionChanged.connect(w.view.filterByMachine)
            self.widgets.append(w)
            self.addTab(w, label)


import sys

def main():
    app = QApplication(sys.argv)  # создаёт основной объект программы
    form = MainWindow()  # создаёт объект формы
    form.show()  # даёт команду на отображение объекта формы и содержимого
    app.exec_()  # запускает приложение

if __name__ == "__main__":
    sys.exit(main()) 
