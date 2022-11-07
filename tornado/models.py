from __future__ import unicode_literals
from django.db import models


class Tornado(models.Model):
    
    tornado_id = models.PositiveIntegerField()
    tnaño1 = models.CharField(max_length=50, default='2019')
    tnaño2 = models.CharField(max_length=50, default='2020')
    tnaño3 = models.CharField(max_length=50, default='2021')
    tncifra1= models.CharField(max_length=50, default='688')
    tncifra2= models.CharField(max_length=50, default='347')
    tncifra3= models.CharField(max_length=50, default='417')


class TornadoDamage(models.Model):
    tornado_id = models.ForeignKey(Tornado,on_delete=models.CASCADE)
    amount = models.DecimalField(max_length=5, max_digits=5, decimal_places=2)
    deaths = models.PositiveIntegerField()
    bridges = models.PositiveIntegerField(default=0)
    house_destroyed = models.PositiveIntegerField()

    def __str__(self):
        return str(self.tornado_id) + ' ' + str(self.amount)+' millions loss'
