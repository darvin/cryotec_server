# -*- coding: utf-8 -*-

from django.db import models
from clients.models import Client

class MachineType(models.Model):
    """
    Тип машины
    """
    name = models.CharField(max_length=30)
    """Название"""
    
    def __unicode__(self):
        return u"%s" % self.name

    
    def get_absolute_url(self):
        return "/machine_tyep%s" % self.name
    
    
class MachineMark(models.Model):
    """
    Марка машины
    """
    name = models.CharField(max_length=30)
    """Название"""
    machinetype = models.ForeignKey(MachineType)
    """Тип машин, к которому принадлежит марка"""
    to_days_max = models.IntegerField()
    motohours_max = models.IntegerField()

    def __unicode__(self):
        return u"%s" % self.name
    
    
    def get_absolute_url(self):
        return "/machine_mark%s" % self.name

class Machine(models.Model):
    """
    Конкретная машина
    """
    serial = models.CharField(max_length=30)
    """Серийный номер машины"""
    client = models.ForeignKey(Client)
    """Клиент, которому продана машина"""
    alias = models.CharField(max_length=30, blank=True)
    """Псевдоним машины"""
    motohours = models.IntegerField()
    machinemark = models.ForeignKey(MachineMark)
    """Марка машины"""
    
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
