# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-18 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='product_title',
            field=models.SlugField(default=None),
        ),
    ]
