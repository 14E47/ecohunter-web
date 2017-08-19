# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-14 13:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20170710_1002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='date',
            new_name='from_date',
        ),
        migrations.AddField(
            model_name='booking',
            name='to_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]