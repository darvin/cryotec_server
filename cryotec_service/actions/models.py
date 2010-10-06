# -*- coding: utf-8 -*-

try:
    from django.contrib.auth.models import User
    
    from django.db import models
except ImportError:
    from qtdjango import models
    User = models.User

from machines.models import Machine
from actiontemplates.models import ReportLevel, ReportTemplate
#
#class ActionManager(models.Manager):
#    def get_by_machine_client_mark(self, machine_pk=None, client_pk=None, machinemark_pk=None):
#        pks = Machine.objects.get_pks_by_machine_client_mark(machine_pk, client_pk, machinemark_pk)
#        return self.filter(machine__pk__in=pks)









class Action(models.Model):
    """
    Отцовский класс для всех событий (действий) - тех-обслуживаний, профосмотров, репортов неисправностей
    и ремонтов.
    """
    
    machine = models.ForeignKey(Machine, verbose_name="Машина")
    """Машина, к которой относится действие"""
    comment = models.TextField("Комментарий", max_length=3000)
    """Текстовое содержание действия - комментарий"""
    date = models.DateField("Дата", auto_now_add=True)
    """Дата/время действия"""
    user = models.ForeignKey(User, verbose_name="Пользователь")
    
#    objects = ActionManager()
    
    
    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"

    
    def __unicode__(self):
        return u"%s: %s" % (self.date.strftime("%d.%m.%y"), self.comment)
    @classmethod
    def get_admin_path(cls):
        print "sdf!"
        print cls.get_real()
        return cls.get_real()
    
    
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
    motohours = models.IntegerField("Моточасы")
    """Моточасы, считанные во время профосмотра с машины"""

    class Meta:
        verbose_name = "Периодическое событие"
        verbose_name_plural = "Периодическое события"


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
    Контроль наработки моточасов - проводится в соответствии с календарным планом
    """
    pass
    class Meta:
        verbose_name = "Контроль моточасов"
        verbose_name_plural = "Контроли моточасов"

    
class Maintenance(PAction):
    """
    Техобслуживание = проводится в соответствии с моточасами
    """    
    pass
    class Meta:
        verbose_name = "Техобслуживание"
        verbose_name_plural = "Техобслуживания"






class Report(Action):
    """
    Сообщение о неисправности
    """
    
    reporttemplate = models.ForeignKey(ReportTemplate, blank=True, null=True, verbose_name="Стандартная неисправность")
    
    maintenance = models.ForeignKey(Maintenance, blank=True, null=True, verbose_name="Техобслуживание")
    """Периодическое действие, во время которого выявлена неисправность"""
    
    

    interest = models.ForeignKey(ReportLevel, verbose_name="Уровень неисправности")
    """Серьезность неисправности"""


    class Meta:
        verbose_name = "Неисправность"
        verbose_name_plural = "Неисправности"

    
    def __unicode__(self):
        return u"%s: %s (%d)" % (self.date.strftime("%d.%m.%y"), self.comment, self.interest.order)
    
        
    def save(self):
        #FIXME
        #if self.reporttemplate is not None:
            #self.interest = self.reporttemplate.interest
        super(Report,self).save()
    
    
class Fix(Action):
    """
    Ремонт
    """
    report = models.ForeignKey(Report, verbose_name="Сообщение о неисправности, ремонт которой проводился")
    """Сообщение о неисправности, ремонт которой проводился"""
    fixed = models.BooleanField("Исправлена")
    """Исправлена ли неисправность"""
    
    class Meta:
        verbose_name = "Ремонт"
        verbose_name_plural = "Ремонты"
