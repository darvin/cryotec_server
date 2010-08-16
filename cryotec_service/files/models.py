# -*- coding: utf-8 -*-

from django.db import models
from actions.models import Action
from clients.models import Client
from machines.models import Machine, MachineMark


def make_upload_path(instance, filename):
    """Generates upload path for FileField"""
    try:
        return u"uploads/actions/%s/%s" % (instance.action.date, filename)
    except AttributeError:
        try:
            return u"uploads/machines/%s/%s" % (instance.machine.name, filename)
        except AttributeError:
            try:
                return u"uploads/machine_makrs/%s/%s" % (instance.machinemark.name, filename)
            except AttributeError:
                try:
                    return u"uploads/clients/%s/%s" % (instance.client.name, filename)
                except AttributeError:
                    return u"uploads/uncategorized/%s" % (filename)






class Upload(models.Model):
    action = models.ForeignKey(Action, verbose_name="Событие", blank=True, null=True)
    machine = models.ForeignKey(Machine, verbose_name="Машина", blank=True, null=True)
    machinemark = models.ForeignKey(MachineMark, verbose_name="Марка машины", blank=True, null=True)
    client = models.ForeignKey(Client, verbose_name="Клиент", blank=True, null=True)
    file = models.FileField("Файл", upload_to=make_upload_path)
    uploaded_date = models.DateTimeField("Дата загрузки", auto_now_add=True)
    
    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
    
    
    def __unicode__(self):
        return "%s" % self.file.name