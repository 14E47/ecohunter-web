# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-15 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0010_auto_20170814_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='practical',
            field=models.TextField(blank=True, verbose_name='Practical'),
        ),
    ]
