# -*- coding: utf-8 -*-
try:
    from django.db import models
except ImportError:
    from qtdjango import models

class Client(models.Model):
    """
    Клиент
    """
    name = models.CharField(u"Имя", max_length=128)
    """Имя клиента"""
    
    comment = models.TextField(u"Комментарий", max_length=3000)

    class Meta:
        verbose_name = u"Клиент"
        verbose_name_plural = u"Клиенты"

    def __unicode__(self):
        return u"%s" % self.name


class ContactFace(models.Model):
    """
    Контактное лицо
    """
    client = models.ForeignKey(Client, verbose_name="Клиент")
    name = models.CharField("Имя", max_length=30)
    phone = models.CharField("Телефон", max_length=30, blank=True)
    email = models.EmailField("E-mail", blank=True)
    
    class Meta:
        verbose_name = "Контактное лицо"
        verbose_name_plural = "Контактное лицо"