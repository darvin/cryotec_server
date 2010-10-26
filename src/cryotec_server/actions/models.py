# -*- coding: utf-8 -*-

try:
    from django.contrib.auth.models import User
    
    from django.db import models
except ImportError:
    from qtdjango import models
    User = models.User

from machines.models import Machine
from actiontemplates.models import ReportLevel, ReportTemplate









class Action(models.Model):
    """
    Отцовский класс для всех событий (действий) - тех-обслуживаний, профосмотров, репортов неисправностей
    и ремонтов.
    """
    
    machine = models.ForeignKey(Machine, verbose_name=u"Машина")
    """Машина, к которой относится действие"""
    comment = models.TextField(u"Комментарий", max_length=3000)
    """Текстовое содержание действия - комментарий"""
    date = models.DateField(u"Дата", auto_now_add=True)
    """Дата/время действия"""
    user = models.ForeignKey(User, verbose_name=u"Пользователь")

    read_only_fields = ["date",]
    auto_user_fields = ["user",]

    class Meta:
        abstract = True
        verbose_name = u"Событие"
        verbose_name_plural = u"События"

    
    def __unicode__(self):
        try:
            return u"%s: %s" % (self.date.strftime("%d.%m.%y"), self.comment)
        except AttributeError:
            return u"%s: %s" % (u"<новая>", self.comment, )





class Checkup(Action):
    """
    Контроль наработки моточасов - проводится в соответствии с календарным планом
    """
    motohours = models.IntegerField(u"Моточасы")
    """Моточасы, считанные во время профосмотра с машины"""
    class Meta:
        verbose_name = u"Контроль моточасов"
        verbose_name_plural = u"Контроли моточасов"



    
class Maintenance(Action):
    """
    Техобслуживание = проводится в соответствии с моточасами
    """    
    pass
    class Meta:
        verbose_name = u"Техобслуживание"
        verbose_name_plural = u"Техобслуживания"






class Report(Action):
    """
    Сообщение о неисправности
    """
    
    reporttemplate = models.ForeignKey(ReportTemplate, blank=True, null=True, verbose_name=u"Стандартная неисправность")
    
    maintenance = models.ForeignKey(Maintenance, blank=True, null=True, verbose_name=u"Техобслуживание")
    """Периодическое действие, во время которого выявлена неисправность"""
    
    

    interest = models.ForeignKey(ReportLevel, verbose_name=u"Уровень неисправности")
    """Серьезность неисправности"""

    include_methods_results = {"is_fixed":models.BooleanField(u"Исправлена")}

    class Meta:
        verbose_name = u"Неисправность"
        verbose_name_plural = u"Неисправности"

    
    def __unicode__(self):
        try:
            date = self.date.strftime("%d.%m.%y")
        except AttributeError:
            date = u"<новая>"
        return u"%s: %s (%d)" % (date, self.comment, self.interest.order)
    
        
    def save(self):
        if self.reporttemplate is not None:
            self.interest = self.reporttemplate.interest
        super(Report,self).save()

    def is_fixed(self):
        try:
            return self.fix_set.order_by("date")[0].fixed
        except IndexError:
            return False
    
class Fix(Action):
    """
    Ремонт
    """
    report = models.ForeignKey(Report, verbose_name=u"Сообщение о неисправности, ремонт которой проводился")
    """Сообщение о неисправности, ремонт которой проводился"""
    fixed = models.BooleanField(u"Исправлена")
    """Исправлена ли неисправность"""
    
    class Meta:
        verbose_name = u"Ремонт"
        verbose_name_plural = u"Ремонты"
