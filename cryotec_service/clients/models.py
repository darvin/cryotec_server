# -*- coding: utf-8 -*-

from django.db import models

class Client(models.Model):
    """
    Клиент
    """
    name = models.CharField(max_length=30)
    """Имя клиента"""

    def __unicode__(self):
        return u"%s" % self.name
