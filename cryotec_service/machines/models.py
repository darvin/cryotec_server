# -*- coding: utf-8 -*-

from django.db import models
from clients.models import Client

class MachineType(models.Model):
    """
    Тип машины
    """
    name = models.CharField("Название типа машин", max_length=30)
    """Название"""
    
    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name = "Тип машины"
        verbose_name_plural = "Типы машин"


    
    def get_absolute_url(self):
        return "/machine_tyep%s" % self.name
    
    
class MachineMark(models.Model):
    """
    Марка машины
    """
    name = models.CharField("Марка", max_length=30)
    """Название"""
    machinetype = models.ForeignKey(MachineType, verbose_name="Тип машин")
    """Тип машин, к которому принадлежит марка"""

    month_default = models.IntegerField("Количество месяцев до следущего профосмотра (по умолчанию)")
    motohours_default = models.IntegerField("Количество моточасов до следующего техобслуживания (по умолчанию)")
    
    class Meta:
        verbose_name = "Марка машины"
        verbose_name_plural = "Марки машин"


    def __unicode__(self):
        return u"%s" % self.name
    
    
    def get_absolute_url(self):
        return "/machine_mark%s" % self.name



class MachineManager(models.Manager):
    def get_pks_by_machine_client_mark(self, machine_pk=None, client_pk=None, machinemark_pk=None):
        ms = self.get_by_machine_client_mark(machine_pk, client_pk, machinemark_pk)
        pks = [m.pk for m in ms]
        return pks
 
    
    def get_by_machine_client_mark(self, machine_pk=None, client_pk=None, machinemark_pk=None):
        if not (machine_pk in (None, -1)):
            m = [self.get(pk=machine_pk)]
        elif not (client_pk in (None, -1)):
            if not (machinemark_pk in (None, -1)):
                m = self.filter(client__pk=client_pk, machinemark__pk=machinemark_pk)
            else:
                m = self.filter(client__pk=client_pk)
        elif not (machinemark_pk in (None, -1)):
            m = self.filter(machinemark__pk=machinemark_pk)
        else:
            m = self.all()
            
        return m

class Machine(models.Model):
    """
    Конкретная машина
    """
    serial = models.CharField("Серийный номер", max_length=30,  blank=True, null=True)
    """Серийный номер машины"""
    client = models.ForeignKey(Client, verbose_name="Клиент, которому принадлежит машина",   related_name="machines")
    customer = models.ForeignKey(Client, verbose_name="Клиент, который купил машину",  blank=True, null=True,  related_name="machines_customer")

    """Клиент, которому продана машина"""
    alias = models.CharField("Псевдоним", max_length=30, blank=True)
    """Псевдоним машины"""
    machinemark = models.ForeignKey(MachineMark, verbose_name="Марка машины")
    """Марка машины"""
    
    month = models.IntegerField("Количество месяцев до следущего профосмотра")
    motohours = models.IntegerField("Количество моточасов до следующего техобслуживания")
    
    
    objects = MachineManager()

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"
    

    def __unicode__(self):
        if self.alias:
            return u"%s" % self.alias
        else:
            return u"%s_%s" % (self.client.name, self.machinemark)
        
    def get_absolute_url(self):
        return "/machine_%s" % self
    
    def get_machinetype_name(self):
        return self.machinemark.machinetype.name
    
    
    def get_machinemark_name(self):
        return self.machinemark.name
    
    def get_machinetype_pk(self):
        return self.machinemark.machinetype.pk
    
    
    def get_machinemark_pk(self):
        return self.machinemark.pk
