# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-18 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0002_experience_product_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='product_title',
            field=models.SlugField(null=True),
        ),
    ]