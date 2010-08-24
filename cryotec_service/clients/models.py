# -*- coding: utf-8 -*-

from django.db import models

class Client(models.Model):
    """
    Клиент
    """
    name = models.CharField("Имя", max_length=30)
    """Имя клиента"""
    
    comment = models.TextField("Комментарий", max_length=3000)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

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