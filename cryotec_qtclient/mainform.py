# -*- coding: utf-8 -*-

'''
@author: darvin
'''

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from views import FixWithButtonsView, ReportWithButtonsView, \
        MaintenanceWithButtonsView, CheckupWithButtonsView, MachineTreeView
from qtdjango.models import Model
from models import mm

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


        syncAction = QAction(u"Синхронизировать", self)
        syncAction.triggered.connect(self.synchronize)

        machinetreepanelAction = dockWidget.toggleViewAction()

        toolbar = self.addToolBar("main")

        toolbar.addAction(machinetreepanelAction)
        toolbar.addAction(syncAction)

        self.mm = mm
        self.mm.add_notify_dumped(self.synced)
        self.mm.add_notify_undumped(self.unsynced)

    def synchronize(self):
        """Synchronizes ModelsManager"""
        self.mm.dump()

    def synced(self):
        self.statusBar().showMessage(u'Синхронизированно')

    def unsynced(self):
        self.statusBar().showMessage(u'Есть несохранненные записи')




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
            w = widget(None)
            machine_tree.modelSelectionChanged.connect(w.filterByMachine)
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
