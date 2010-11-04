# -*- coding: utf-8 -*-
try:
    from libs.modelmixins import UrlMixin
except ImportError:
    from cryotec_server.libs.modelmixins import UrlMixin
try:
    from django.db import models
except ImportError:
    from qtdjango import models
from machines.models import MachineMark
from actions.models import Maintenance

class ChecklistQuestion(models.Model):
    """
    Вопрос чеклиста
    """
    comment = models.CharField(u"Текст вопроса",max_length=100)
    """Содержание вопроса"""
    machinemark = models.ManyToManyField(MachineMark, verbose_name=u"Марка машин, к которым относится вопрос чеклиста")
    """Марка машин, к которым относится вопрос чеклиста"""
    required = models.BooleanField(u"Требуемый")
    """Необходим ли ответ для вопроса"""
    order = models.PositiveIntegerField(u"Порядковый номер в чеклисте")
    """Порядковый номер в чеклисте"""

    dump_order = -1

    class Meta:
        verbose_name = u"Чеклист-вопрос"
        verbose_name_plural = u"Чеклист-вопросы"

    
    def __unicode__(self):
        return u"%d. %s" % (self.order, self.comment)
        
    
class ChecklistAnswer(models.Model):
    """
    Ответ на вопрос чеклиста
    """
    checklistquestion = models.ForeignKey(ChecklistQuestion, verbose_name=u"Вопрос к этому ответу")
    """Вопрос к этому ответу"""
    maintenance = models.ForeignKey(Maintenance, blank=True, null=True, verbose_name=u"Техобслуживание")
    """Переодическое проверка, в результате которой получен ответ"""
    comment = models.TextField(u"Текстовый комментарий",max_length=300)
    """Текстовый комментарий"""

    dump_order = 100

    def __unicode__(self):
        return u"%d. %s" % (self.checklistquestion.order, self.comment)
    
    class Meta:
        ordering = ['checklistquestion__order']
        
        verbose_name = u"Чеклист-ответ"
        verbose_name_plural = u"Чеклист-ответы"


    
