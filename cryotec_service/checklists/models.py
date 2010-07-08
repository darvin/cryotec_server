# -*- coding: utf-8 -*-

from django.db import models
from machines.models import MachineMark
from actions.models import PAction

class ChecklistQuestion(models.Model):
    """
    Вопрос чеклиста
    """
    comment = models.CharField(max_length=100)
    """Содержание вопроса"""
    machinemark = models.ForeignKey(MachineMark)
    """Марка машин, к которым относится вопрос чеклиста"""
    required = models.BooleanField()
    """Необходим ли ответ для вопроса"""
    order = models.PositiveIntegerField()
    """Порядковый номер в чеклисте"""
    
    def __unicode__(self):
        return u"%d. %s" % (self.order, self.comment)
    
class ChecklistAnswer(models.Model):
    """
    Ответ на вопрос чеклиста
    """
    checklistquestion = models.ForeignKey(ChecklistQuestion)
    """Вопрос к этому ответу"""
    paction = models.ForeignKey(PAction)
    """Переодическое проверка, в результате которой получен ответ"""
    comment = models.CharField(max_length=300)
    """Текстовый комментарий"""

    def __unicode__(self):
        return u"%d. %s" % (self.checklistquestion.order, self.comment)
    
    class Meta:
        ordering = ['checklistquestion__order']

    