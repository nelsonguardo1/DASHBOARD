from __future__ import unicode_literals
from django.db import models


class Earthquake(models.Model):
    earthquake_id = models.PositiveIntegerField(primary_key='true')
    eaño1 = models.CharField(max_length=50, default='2019')
    eaño2 = models.CharField(max_length=50, default='2020')
    eaño3 = models.CharField(max_length=50, default='2021')
    ecifra1= models.CharField(max_length=50, default='383')
    ecifra2= models.CharField(max_length=50, default='427')
    ecifra3= models.CharField(max_length=50, default='462')

class Tsunami(models.Model):
    tsunami_id = models.PositiveIntegerField(primary_key='true')
    tsaño1 = models.CharField(max_length=50, default='2019')
    tsaño2 = models.CharField(max_length=50, default='2020')
    tsaño3 = models.CharField(max_length=50, default='2021')
    tscifra1= models.CharField(max_length=50, default='197')
    tscifra2= models.CharField(max_length=50, default='223')
    tscifra3= models.CharField(max_length=50, default='246')


class VolcanicEruption(models.Model):
    
    volcano_id = models.PositiveIntegerField(primary_key='true')
    año1 = models.CharField(max_length=50, default='2019')
    año2 = models.CharField(max_length=50, default='2020')
    año3 = models.CharField(max_length=50, default='2021')
    cifra1= models.CharField(max_length=50, default='42')
    cifra2= models.CharField(max_length=50, default='37')
    cifra3= models.CharField(max_length=50, default='26')

class EarthquakeDamage(models.Model):
    earthquake_id = models.OneToOneField(Earthquake, primary_key='true', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, max_length=5, decimal_places=2)
    deaths = models.PositiveIntegerField()
    house_destroyed = models.PositiveIntegerField()
    bridges_destroyed = models.PositiveIntegerField(default=2)

    def __str__(self):
        return str(self.earthquake_id)+' '+str(self.amount)+' '+'million of damage'


class TsunamiDamage(models.Model):
    tsunami_id = models.OneToOneField(Tsunami, primary_key='true', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, max_length=5, decimal_places=2)
    deaths = models.PositiveIntegerField()
    house_destroyed = models.PositiveIntegerField()
    bridge_destroyed = models.PositiveIntegerField(default=2)

    def __str__(self):
        return str(self.tsunami_id)+' '+str(self.amount)+' '+'million of damage'


class VolcanoDamage(models.Model):
    volcano_id = models.OneToOneField(VolcanicEruption, primary_key='true', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, max_length=5, decimal_places=2)
    deaths = models.PositiveIntegerField()
    house_destroyed = models.PositiveIntegerField()

    def __str__(self):
        return str(self.volcano_id)+' '+str(self.amount)+' '+'million of damage'


class QuakeTsunami(models.Model):
    tsunami_id = models.OneToOneField(Tsunami, on_delete=models.CASCADE)
    earthquake_id = models.ForeignKey(Earthquake, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.earthquake_id)+' '+str(self.tsunami_id)


class VolcanoTsunami(models.Model):
    tsunami_id = models.ForeignKey(Tsunami, on_delete=models.CASCADE)
    volcano_id = models.ForeignKey(VolcanicEruption, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.volcano_id)+' '+str(self.tsunami_id)
