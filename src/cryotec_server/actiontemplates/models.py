# -*- coding: utf-8 -*-

try:
    from libs.modelmixins import UrlMixin
except ImportError:
    from cryotec_server.libs.modelmixins import UrlMixin
try:
    from django.db import models
except ImportError:
    from qtdjango import models
    
import machines.models

class ReportLevel(models.Model):
    name = models.CharField("Название", max_length=30)
    order = models.IntegerField("Числовое выражение уровня")
    class Meta:
        verbose_name = "Уровень неисправность"
        verbose_name_plural = "Уровни неисправности"

    def __unicode__(self):
        return u"%s (%d)" % (self.name, self.order)



class ReportTemplate(models.Model):
    name = models.CharField("Заголовок", max_length=64)

    machinemark = models.ForeignKey(machines.models.MachineMark, verbose_name="Марка машины")
    """Марка машины, к которой относится действие"""
    comment = models.TextField("Комментарий", max_length=3000)   
    
    interest = models.ForeignKey(ReportLevel, verbose_name="Уровень неисправности")
    """Серьезность неисправности"""
    
    class Meta:
        verbose_name = "Стандартная неисправность"
        verbose_name_plural = "Стандартные неисправности"

    def __unicode__(self):
        return u"%s (%d)" % (self.name, self.interest.order)
 
