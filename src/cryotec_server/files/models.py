# -*- coding: utf-8 -*-
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

try:
    from django.db import models
except ImportError:
    from qtdjango import models
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
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    related_to = generic.GenericForeignKey()
    file = models.FileField("Файл", upload_to=make_upload_path)
    uploaded_date = models.DateTimeField("Дата загрузки", auto_now_add=True)
    
    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
    
    
    def __unicode__(self):
        return "%s" % self.file.name