# -*- coding: UTF-8 -*-

from qtdjango.detailviews import *
from qtdjango.undetailviews import *
from models import *
from PyQt4 import QtCore

class MachinesTableView(TableView):
#    fields = ["alias","serial"]
    model = Machine


class MachineTreeView(TreeView):
    model = Machine
    tree = (
            ("customer", Client),
            ("machinemark", MachineMark),
           )
    fields = "__unicode__"



class ActionView(TableView):
    def __init__(self):
        """docstring for __init__"""
        super(ActionView, self).__init__()

    @QtCore.pyqtSlot(Model)
    def filterByMachine(self, machine):
        self.set_filter({"machine":machine})


class ReportDetailView(DetailView):
    model = Report

class ReportView(ActionView):
    model = Report
    detail_view = ReportDetailView

class ReportWithButtonsView(UndetailWithButtonsView):
    edit_dumped = False
    viewclass = ReportView


class FixDetailView(DetailView):
    model = Fix

class FixView(ActionView):
    model = Fix
    detail_view = FixDetailView

class FixWithButtonsView(UndetailWithButtonsView):
    edit_dumped = False
    viewclass = FixView


class MaintenanceDetailView(DetailView):
    model = Maintenance

class MaintenanceView(ActionView):
    model = Maintenance
    detail_view = MaintenanceDetailView

class MaintenanceWithButtonsView(UndetailWithButtonsView):
    edit_dumped = False
    viewclass = MaintenanceView


class CheckupDetailView(DetailView):
    model = Checkup

class CheckupView(ActionView):
    model = Checkup
    detail_view = CheckupDetailView

class CheckupWithButtonsView(UndetailWithButtonsView):
    edit_dumped = False
    viewclass = CheckupView

