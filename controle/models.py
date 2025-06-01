from django.db import models
from datetime import timezone, date, datetime

class Uber(models.Model):
    data_criacao =models.DateField(None)
    created_at=models.DateTimeField(default=datetime.now)
    gasolina = models.FloatField()
    ganho = models.FloatField()
    km = models.FloatField()
    

    def resultado(self,*args, **kwargs):
        self.ganho = (self.ganho-self.gasolina)
        
        
        

    

# Create your models here.
