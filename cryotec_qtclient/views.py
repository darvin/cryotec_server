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



class ChecklistInlineView(QFrame, UndetailView):
    model = ChecklistAnswer

    def __init__(self, filter):
        """docstring for __init__"""
        QFrame.__init__(self)
        self._widgets =[]
        self.formlayout = QFormLayout()
        self.setLayout(self.formlayout)
        UndetailView.__init__(self, filter)
        self.set_filter(filter)

    def __clean(self):
        """Deletes all old widgets"""
        pass

    def set_filter(self, filter):
        """Creates all widgets when we sets filter"""
        self.__clean()
#        print filter["paction"], "#######"
        machine = filter["paction"].machine
#        print machine
        mmark = machine.machinemark
        questions =[q for q in ChecklistQuestion.filter(machinemark=mmark)]
#        for q in questions:
#            print unicode(q), ChecklistAnswers.filter(maitenance=filter["paction"],\
#                                               checklistquestion=q)


    def save(self):
        pass




class ActionView(TableView):
    def __init__(self, filter):
        """docstring for __init__"""
        super(ActionView, self).__init__(filter)

    @QtCore.pyqtSlot(Model)
    def filterByMachine(self, machine):
        self.set_filter({"machine":machine})


class FixDetailView(DetailView):
    model = Fix

class FixView(ActionView):
    model = Fix
    detail_view = FixDetailView

class FixWithButtonsView(UndetailWithButtonsView):
    edit_dumped = False
    viewclass = FixView


class ReportDetailView(DetailView):
    model = Report
    inline_views = ((FixWithButtonsView, "report", u"Ремонты этой неисправности"),)

class ReportView(ActionView):
    model = Report
    detail_view = ReportDetailView

class ReportWithButtonsView(UndetailWithButtonsView):
    edit_dumped = False
    viewclass = ReportView


class MaintenanceDetailView(DetailView):
    model = Maintenance
    inline_views = ((ChecklistInlineView, "paction", u"Ответы на чеклист"),)

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

