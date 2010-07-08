# -*- coding: utf-8 -*-

from django.db import models
from machines.models import Machine


class ActionManager(models.Manager):
    def get_by_machine_client_mark(self, machine_pk=None, client_pk=None, machinemark_pk=None):
        pks = Machine.objects.get_pks_by_machine_client_mark(machine_pk, client_pk, machinemark_pk)
        return self.filter(machine__pk__in=pks)



class Action(models.Model):
    """
    Отцовский класс для всех событий (действий) - тех-обслуживаний, профосмотров, репортов неисправностей
    и ремонтов.
    """
    machine = models.ForeignKey(Machine)
    """Машина, к которой относится действие"""
    comment = models.CharField(max_length=3000)
    """Текстовое содержание действия - комментарий"""
    date = models.DateField()
    """Дата/время действия"""
    
    objects = ActionManager()
    
    def __unicode__(self):
        return u"%s: %s" % (self.date.strftime("%d.%m.%y"), self.comment)
    
    def get_real(self):
        try:
            return self.report
        except Report.DoesNotExist:
            pass
        try:
            return self.fix
        except Fix.DoesNotExist:
            pass
        try:
            if self.paction:
                return self.paction.get_real()
        except PAction.DoesNotExist:
            pass


class PAction(Action):
    """
    Отцовский класс для периодических действий
    """
    pass
    def get_real(self):
        try:
            return self.checkup
        except Checkup.DoesNotExist:
            pass
        try:
            return self.maintenance
        except Maintenance.DoesNotExist:
            pass

class Checkup(PAction):
    """
    Профосмотр - проводится в соответствии с календарным планом
    """
    motohours = models.IntegerField()
    """Моточасы, считанные во время профосмотра с машины"""

    
class Maintenance(PAction):
    """
    Техобслуживание = проводится в соответствии с моточасами
    """    
    pass


class Report(Action):
    """
    Сообщение о неисправности
    """
    paction = models.ForeignKey(PAction, blank=True, null=True)
    """Периодическое действие, во время которого выявлена неисправность"""
    fixed = models.BooleanField()
    """Исправлена ли неисправность. Изначально - не исправлена. Опциональное"""
    by_client = models.BooleanField()
    """сообщено клиентом. Изначально - отрицательно. Опциональное"""
    
    INTERESTS_CHOICES = (
            (0, 'Сообщение'),
            (1, 'Мелкая поломка'),
            (2, 'Средняя поломка'),
            (3, 'Серьезная неисправность'),
            (4, 'Полный отказ'),
    )
    interest = models.PositiveSmallIntegerField(choices=INTERESTS_CHOICES, default=0)
    """Серьезность неисправности"""
    
    def __unicode__(self):
        return u"%s: %s (%d)" % (self.date.strftime("%d.%m.%y"), self.comment, self.interest)
    
    
class Fix(Action):
    """
    Ремонт
    """
    report = models.ForeignKey(Report)
    """Сообщение о неисправности, ремонт которой проводился"""
