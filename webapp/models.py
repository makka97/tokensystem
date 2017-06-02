from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Vendor(models.Model):
    vendorName = models.CharField(max_length=100)

    def __unicode__(self):  
        return self.vendorName

class Barcode(models.Model):
    employeeId = models.IntegerField()
    barcodeName = models.CharField(max_length=500)
    barcode = models.CharField(max_length=50)

    def __unicode__(self): 
        return self.barcode

class Token(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    barcode = models.ForeignKey(Barcode, on_delete=models.CASCADE)
    tokenDateTime = models.DateTimeField()




