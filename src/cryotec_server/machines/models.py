# -*- coding: utf-8 -*-
try:
    from django.db import models
except ImportError:
    from qtdjango import models
from clients.models import Client

class MachineType(models.Model):
    """
    Тип машины
    """
    name = models.CharField("Название типа оборудования", max_length=30)
    """Название"""

    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name = u"Тип оборудования"
        verbose_name_plural = u"Типы оборудования"



    
    
class MachineMark(models.Model):
    """
    Марка машины
    """
    name = models.CharField("Марка", max_length=90)
    """Название"""
    machinetype = models.ForeignKey(MachineType, verbose_name="Тип оборудования")
    """Тип машин, к которому принадлежит марка"""

    month_default = models.IntegerField("Количество месяцев между профосмотрами (по умолчанию)", blank=True, null=True)
    motohours_default = models.IntegerField("Количество моточасов между техобслуживаниями (по умолчанию)", blank=True, null=True)
    
    class Meta:
        verbose_name = "Марка оборудования"
        verbose_name_plural = "Марки оборудования"


    def __unicode__(self):
        return u"%s" % self.name
    
    

class Machine(models.Model):
    """
    Конкретная машина
    """
    serial = models.CharField("Серийный номер", max_length=30,  blank=True, null=True)
    """Серийный номер машины"""
    client = models.ForeignKey(Client, verbose_name="Клиент, которому принадлежит оборудование",   related_name="machines")
    customer = models.ForeignKey(Client, verbose_name="Клиент, который купил оборудование",  blank=True, null=True,  related_name="machines_customer")

    """Клиент, которому продана машина"""
    alias = models.CharField("Псевдоним", max_length=30, blank=True)
    """Псевдоним машины"""
    machinemark = models.ForeignKey(MachineMark, verbose_name="Марка оборудования")
    """Марка машины"""
    
    month = models.IntegerField("Количество месяцев между профосмотрами", blank=True, null=True)
    motohours = models.IntegerField("Количество моточасов между техобслуживаниями", blank=True, null=True)

    include_methods_results = ["get_current_motohours", "get_last_checkup_date"]

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
        return self.checkup_set.order_by("date")[0].motohours


    def get_last_checkup_date(self):
        return self.checkup_set.order_by("date")[0].date