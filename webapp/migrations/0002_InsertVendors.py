from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
       migrations.RunSQL("INSERT INTO webapp_Vendor (id, vendorName) VALUES (1, 'V1');"),
       migrations.RunSQL("INSERT INTO webapp_Vendor (id, vendorName) VALUES (2, 'V2');"),
    ]