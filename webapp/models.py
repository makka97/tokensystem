from __future__ import unicode_literals

from django.db import models
from django.db import connection


# Create your models here.
class TokenManager(models.Manager):
    def all(self):
        #Create Query
        cursor = connection.cursor()
        cursor.execute("""select t.vendor_id, date(t.tokenDateTime), count(*) from webapp_token t group by t.vendor_id, date(t.tokenDateTime)""")

        #Execute Query
        result_list = []
        for tokenDets in cursor.fetchall():
            #Create model instance
            v = Vendor.objects.get(id = tokenDets[0])
            tokenDet = self.model(vendor = v, tokenDateTime = tokenDets[1])

            #Add new attribute to model
            tokenDet.num_count = tokenDets[2]

            result_list.append(tokenDet)
        
        #Return model instances
        return result_list

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

    objects = models.Manager()
    

class DailyCountOfTokens(Token):
    class Meta:
        proxy = True

    objects = TokenManager()



