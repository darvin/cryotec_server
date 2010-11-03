# -*- coding: utf-8 -*-
from libs.modelmixins import UrlMixin

try:
    from django.db import models
except ImportError:
    from qtdjango import models
from clients.models import Client

class MachineType(models.Model, UrlMixin):
    """
    Тип машины
    """
    name = models.CharField(u"Название типа оборудования", max_length=128)
    """Название"""



    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name = u"Тип оборудования"
        verbose_name_plural = u"Типы оборудования"



    
    
class MachineMark(models.Model, UrlMixin):
    """
    Марка машины
    """
    name = models.CharField(u"Марка", max_length=128)
    """Название"""
    machinetype = models.ForeignKey(MachineType, verbose_name=u"Тип оборудования")
    """Тип машин, к которому принадлежит марка"""

    month_default = models.IntegerField(u"Количество месяцев между профосмотрами (по умолчанию)", blank=True, null=True)
    motohours_default = models.IntegerField(u"Количество моточасов между техобслуживаниями (по умолчанию)", blank=True, null=True)



    class Meta:
        verbose_name = u"Марка оборудования"
        verbose_name_plural = u"Марки оборудования"


    def __unicode__(self):
        return u"%s" % self.name
    



class Machine(models.Model, UrlMixin):
    """
    Конкретная машина
    """
    serial = models.CharField(u"Серийный номер", max_length=128,  blank=True, null=True)
    """Серийный номер машины"""
    client = models.ForeignKey(Client, verbose_name=u"Клиент, которому принадлежит оборудование",   related_name="machines")
    customer = models.ForeignKey(Client, verbose_name=u"Клиент, который купил оборудование",  blank=True, null=True,  related_name="machines_customer")

    """Клиент, которому продана машина"""
    alias = models.CharField(u"Псевдоним", max_length=128, blank=True)
    """Псевдоним машины"""
    machinemark = models.ForeignKey(MachineMark, verbose_name=u"Марка оборудования")
    """Марка машины"""

    date = models.DateField(u"Дата ввода в эксп.")
    """Дата ввода в эксплуатацию оборудования"""

    month = models.IntegerField(u"Количество месяцев между профосмотрами", blank=True, null=True)
    motohours = models.IntegerField(u"Количество моточасов между техобслуживаниями", blank=True, null=True)


    class Meta:
        verbose_name = u"Оборудование"
        verbose_name_plural = u"Оборудование"
    

    def __unicode__(self):
        if self.alias:
            return u"%s" % self.alias
        else:
            return u"%s_%s" % (self.client.name, self.machinemark)
        

    
    def save(self):
        if self.customer == None:
            self.customer = self.client
        super(Machine,self).save()


    def get_current_motohours(self):
        try:
            return self.checkup_set.order_by("date")[0].motohours
        except IndexError:
            return 0

    get_current_motohours.method_as_field = models.IntegerField(u"Моточасы", blank=True, null=True)


    def get_last_checkup_date(self):
        try:
            return self.checkup_set.order_by("date")[0].date
        except IndexError:
            return self.date


    get_last_checkup_date.method_as_field = models.DateField(u"Дата последнего считывания", auto_now_add=True),