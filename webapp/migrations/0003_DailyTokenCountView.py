from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_InsertVendors'),
    ]

    operations = [
       migrations.RunSQL("create view webapp_DailyCountOfToken as select v.vendorName as vendor_name, date(t.tokenDateTime) as token_date, count(*) as num_count from webapp_token t, webapp_vendor v where v.id = t.vendor_id group by v.vendorName, date(t.tokenDateTime);"),
    ]