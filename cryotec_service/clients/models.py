# -*- coding: utf-8 -*-

from django.db import models

class Client(models.Model):
    """
    Клиент
    """
    name = models.CharField("Имя", max_length=30)
    """Имя клиента"""
    
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __unicode__(self):
        return u"%s" % self.name
