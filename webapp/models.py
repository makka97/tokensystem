from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Vendor(models.Model):
    vendorName = models.CharField(max_length=100)

def __unicode__(self):  
    return self.Vendor

class Barcode(models.Model):
    barcode = models.IntegerField(default=0)
    barcodeName = models.CharField(max_length=500)

def __unicode__(self): 
    return self.Barcode

class Token(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    barcode = models.ForeignKey(Barcode, on_delete=models.CASCADE)
    tokenDateTime = models.DateTimeField()

def __unicode__(self): 
    return self.Token



