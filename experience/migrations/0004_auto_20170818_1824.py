# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-18 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0003_auto_20170818_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='product_title',
            field=models.CharField(default=None, max_length=50),
        ),
    ]