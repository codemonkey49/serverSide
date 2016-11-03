from __future__ import unicode_literals

from django.db import models

# Create your models here.


class watchedData(models.Model):
    userWatched=models.BooleanField()
    machineWatched=models.BooleanField()
    itemID=models.IntegerField()
class itemData(models.Model):
    itemID=models.IntegerField()
    date=models.DateField(auto_now=True)
    price=models.IntegerField()
class transactionData(models.Model):
    PID=models.IntegerField()
    bs=models.BooleanField()
    itemID=models.IntegerField()
    amt=models.IntegerField()
    price=models.IntegerField()
    currentLiquid=models.IntegerField()
class stockData(models.Model):
    PID=models.IntegerField()
    itemID=models.IntegerField()
    amt=models.IntegerField()
    price=models.IntegerField()
class commandsDB(models.Model):
    PID=models.IntegerField()
    bs=models.BooleanField()
    itemID=models.IntegerField()
    amt=models.IntegerField()
    price=models.IntegerField()
    