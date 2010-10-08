# -*- coding: UTF-8 -*-

from qtdjango.views import *
from models import *
from PyQt4 import QtCore

class MachinesTableView(TableView):
#    fields = ["alias","serial"]
    model = Machine


class MachineTreeView(ListView):
    model = Machine
    tree = {"customer":Client,

           }



class ActionView(TableView):
    def __init__(self, machine_tree):
        """docstring for __init__"""
        super(ActionView, self).__init__()
        self.machine_tree = machine_tree
        self.machine_tree.modelSelectionChanged.connect(self.filterByMachine)

    @QtCore.pyqtSlot(Model)
    def filterByMachine(self, machine):
        print machine
        self.set_filter({"machine":machine})


class ReportDetailView(DetailView):
    model = Report

class ReportView(ActionView):
    model = Report
    detail_view = ReportDetailView

class ReportWithButtonsView(UndetailWithButtonsView):
    viewclass = ReportView


class FixDetailView(DetailView):
    model = Fix

class FixView(ActionView):
    model = Fix
    detail_view = FixDetailView

class FixWithButtonsView(UndetailWithButtonsView):
    viewclass = FixView


class MaintenanceDetailView(DetailView):
    model = Maintenance

class MaintenanceView(ActionView):
    model = Maintenance
    detail_view = MaintenanceDetailView

class MaintenanceWithButtonsView(UndetailWithButtonsView):
    viewclass = MaintenanceView


class CheckupDetailView(DetailView):
    model = Checkup

class CheckupView(ActionView):
    model = Checkup
    detail_view = CheckupDetailView

class CheckupWithButtonsView(UndetailWithButtonsView):
    viewclass = CheckupView

