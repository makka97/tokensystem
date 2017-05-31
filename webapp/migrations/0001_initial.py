# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-30 11:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeId', models.IntegerField()),
                ('barcodeName', models.CharField(max_length=500)),
                ('barcode', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tokenDateTime', models.DateTimeField()),
                ('barcode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Barcode')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendorName', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='token',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Vendor'),
        ),
        migrations.CreateModel(
            name='TokenPerDay',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('webapp.token',),
        ),
    ]
