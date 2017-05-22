from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

import datetime
from datetime import timedelta

from webapp.models import Vendor, Token, Barcode

def insertValue(apps,schema_editor):
	startDate = datetime.datetime.now().date()
	endDate = startDate + timedelta(days=365)
	
	while (startDate <= endDate):
		vendorInst = Vendor.objects.get(id=1)
		tokenInsert = Token(tokenCount = 0, tokenDate = startDate, vendor = vendorInst) 
		startDate = startDate + timedelta(days=1)
		tokenInsert.save()


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_InsertVendors'),
    ]

    operations = [
     	migrations.RunPython(insertValue),
    ]