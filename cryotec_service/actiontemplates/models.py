from django.db import models
from machines.models import MachineMark

class ReportLevel(models.Model):
    name = models.CharField("Название", max_length=30)



class ReportTemplate(models.Model):
    machinemark = models.ForeignKey(MachineMark, verbose_name="Марка машины")
    """Марка машины, к которой относится действие"""
    comment = models.TextField("Комментарий", max_length=3000)   
    
    interest = models.ForeignKey(ReportLevel, verbose_name="Уровень неисправности")
    """Серьезность неисправности"""
    
    class Meta:
        verbose_name = "Стандартная неисправность"
        verbose_name_plural = "Стандартные неисправности"

    def __unicode__(self):
        return u"%s (%d)" % (self.comment, self.interest)
 
