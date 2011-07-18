# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
try:
    from libs.modelmixins import UrlMixin
except ImportError:
    from cryotec_server.libs.modelmixins import UrlMixin

try:
    from django.contrib.auth.models import User
    
    from django.db import models
except ImportError:
    from qtdjango import models
    User = models.User

from machines.models import Machine
from actiontemplates.models import ReportLevel, ReportTemplate
from clients.models import ContactFace


def smart_truncate(s, width=40):
    try:
        if s[width].isspace():
            return s[0:width];
        else:
            return s[0:width].rsplit(None, 1)[0]
    except IndexError:
        return s





class Action(models.Model, UrlMixin):
    """
    Отцовский класс для всех событий (действий) - тех-обслуживаний, профосмотров, репортов неисправностей
    и ремонтов.
    """
    
    machine = models.ForeignKey(Machine, verbose_name=u"Оборудование")
    """Машина, к которой относится действие"""
    comment = models.TextField(u"Примечание", max_length=3000)
    """Текстовое содержание действия - комментарий"""
    date = models.DateTimeField(u"Дата")
    """Дата/время действия"""
    user = models.ForeignKey(User, verbose_name=u"Автор")

#    read_only_fields = ["date",]
    auto_user_fields = ["user",]

    class Meta:
        abstract = True
        verbose_name = u"Событие"
        verbose_name_plural = u"События"

    
    def __unicode__(self):
        try:
            return smart_truncate(u"%s: %s" % (self.date.strftime("%d.%m.%y"), self.comment))
        except AttributeError:
            return smart_truncate(u"%s: %s" % (u"<новая>", self.comment, ))

    def clean(self):
        if self.machine is None:
            raise ValidationError(u"Не выбранна единица оборудования!")



class Checkup(Action):
    """
    Контроль наработки моточасов - проводится в соответствии с календарным планом
    """
    motohours = models.IntegerField(u"Моточасы")
    """Моточасы, считанные во время профосмотра с машины"""
    class Meta:
        verbose_name = u"Контроль моточасов"
        verbose_name_plural = u"Контроли моточасов"


    def clean(self):
       from django.core.exceptions import ValidationError
       if self.machine.get_current_motohours()>self.motohours:
           raise ValidationError(u"Введенные моточасы не могут быть меньше текущих моточасов машины")


    
class Maintenance(Action):
    """
    Техобслуживание = проводится в соответствии с моточасами
    """
    engineers = models.ManyToManyField(User, verbose_name=u"Сервис-инженеры", related_name="maintenances_by")
    next_date = models.DateTimeField(u"Ориентир. срок очередной замены")
    name = models.TextField(u"Выполненные работы, результат", max_length=3000)
    needed_time = models.TextField(u"Затраты времени", max_length=3000)
    needed_resources = models.TextField(u"Затраты материалов", max_length=3000)
    motohours = models.IntegerField(u"Наработка часов установки к моменту выполнения работ")
    operation_mode = models.TextField(u"Режим работы установки (час/дн, час/мес)", max_length=3000)

    class Meta:
        verbose_name = u"Техобслуживание"
        verbose_name_plural = u"Техобслуживания"

    def extra_to_html(self):
        answers = self.checklistanswer_set()

        html = u""
        for answer in answers:
            a = answer.comment
            q = answer.checklistquestion.comment
            html += u"<b>%s</b>: <i>%s</i><br>"%(q, a)

        return html






class Report(Action):
    """
    Сообщение о неисправности
    """
    name = models.TextField(u"Рекламация/неисправность, способ извещения, от кого поступила", max_length=3000)
    info = models.TextField(u"Сбои и неисправности, выявленные дистанционно или после диагностики на месте", max_length=3000)

    reporttemplate = models.ForeignKey(ReportTemplate, blank=True, null=True, verbose_name=u"Стандартная неисправность")
    
    source_maintenance = models.ForeignKey(Maintenance, blank=True, null=True, verbose_name=u"Источник (Техобслуживание)", related_name="source_for_reports")
    source_contactface = models.ForeignKey(ContactFace, verbose_name=u"Источник (Контактное лицо клиента)", blank=True, null=True, related_name="source_for_reports")
    source_user = models.ForeignKey(User, verbose_name=u"Источник (Сервис-инженер)", blank=True, null=True, related_name="source_for_reports")


    interest = models.ForeignKey(ReportLevel, verbose_name=u"Уровень неисправности")
    """Серьезность неисправности"""


    class Meta:
        verbose_name = u"Неисправность"
        verbose_name_plural = u"Неисправности"

    
    def __unicode__(self):
        try:
            date = self.date.strftime("%d.%m.%y")
        except AttributeError:
            date = u"<новая>"
        return smart_truncate(u"%s: %s (%d)" % (date, self.comment, self.interest.order))
    
        
    def save(self):
        if self.reporttemplate is not None:
            self.interest = self.reporttemplate.interest
        super(Report,self).save()

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.source_maintenance is not None and self.source_maintenance.machine!=self.machine:
            raise ValidationError(u"Выбранно неверное техобслуживание другой машины")

    def is_fixed(self):
        try:
            return self.fix_set.order_by("date")[0].fixed
        except IndexError:
            return False

    is_fixed.method_as_field = models.BooleanField(u"Исправлена")
    is_fixed.short_description = u"Исправлена"

    def source(self):
        for sourcefield in ("source_maintenance", "source_contactface", "source_user"):
            if getattr(self, sourcefield):
                return unicode(getattr(self, sourcefield))

    source.method_as_field = models.CharField(u"Источник")
    source.short_description = u"Источник"
    
class Fix(Action):
    """
    Ремонт
    """
    name = models.TextField(u"Выполненные работы, результат", max_length=3000)
    report = models.ForeignKey(Report, verbose_name=u"Рекламация/неисправность")
    """Сообщение о неисправности, ремонт которой проводился"""
    fixed = models.BooleanField(u"Исправлена")
    """Исправлена ли неисправность"""


    needed_time = models.TextField(u"Затраты времени", max_length=3000)
    needed_resources = models.TextField(u"Затраты материалов", max_length=3000)
    engineers = models.ManyToManyField(User, verbose_name=u"Сервис-инженеры", related_name="fixes_by")

    class Meta:
        verbose_name = u"Ремонт"
        verbose_name_plural = u"Ремонты"

    def clean(self):
        if self.report is not None and self.report.machine!=self.machine:
            raise ValidationError(u"Выбранно неверное сообщение о неисправности другой машины")
