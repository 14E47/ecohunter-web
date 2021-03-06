# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-10 09:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_update_email_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogue', '0009_slugfield_noop'),
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableRooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rooms', models.CharField(max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('rooms', models.CharField(max_length=2)),
                ('guests', models.CharField(max_length=2)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='order',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='product',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='user',
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
    ]
