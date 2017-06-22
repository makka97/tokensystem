from __future__ import unicode_literals

from django.db import models
from django.db import connection


# Create your models here.

class Vendor(models.Model):
    vendorName = models.CharField(max_length=100)

    def __unicode__(self):  
        return self.vendorName

class Barcode(models.Model):
    employeeId = models.IntegerField(default = 0)
    barcodeName = models.CharField(max_length=500)
    barcode = models.CharField(max_length=50)

    def __unicode__(self): 
        return self.barcode

class Token(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    barcode = models.ForeignKey(Barcode, on_delete=models.CASCADE)
    tokenDateTime = models.DateTimeField()

class DailyCountOfToken(models.Model):
    num_count = models.IntegerField(default = 0)
    #vendor_id = models.IntegerField(default = 0, primary_key=True)
    vendor_name = models.CharField(max_length=50, primary_key=True)
    token_date = models.DateField(primary_key=True)

    class Meta:
        managed = False
        unique_together = ('vendor_name', 'token_date')
   


