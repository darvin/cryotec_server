# -*- coding: utf-8 -*-

from django.db import models

class Client(models.Model):
    """
    Клиент
    """
    name = models.CharField("Имя", max_length=30)
    """Имя клиента"""
    
    ur_addr = models.CharField("Юридический адрес", max_length=30)
    post_addr = models.CharField("Почтовый адрес", max_length=30)
    phone = models.CharField("Телефон", max_length=30)
    inn = models.CharField("ИНН", max_length=30)
    kpp = models.CharField("КПП", max_length=30)
    okpo = models.CharField("Код организации по ОКПО", max_length=30)
    rasch_schet = models.CharField("Расчетный счет №", max_length=30)
    kor_schet = models.CharField("Корреспондентский счет №", max_length=30)
    bank = models.CharField("Полное наименование банка", max_length=30)
    bik = models.CharField("БИК", max_length=30)
    director = models.CharField("Ответственное лицо", max_length=30)
    
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __unicode__(self):
        return u"%s" % self.name
