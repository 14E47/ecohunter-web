# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-18 14:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('duration', models.CharField(default=None, max_length=50)),
                ('seats', models.CharField(default=None, max_length=50)),
                ('slot', models.CharField(default=None, max_length=50)),
                ('activity', models.CharField(default=None, max_length=50)),
                ('the_experience', models.TextField(blank=True, null=True)),
                ('the_activity', models.TextField(blank=True, null=True)),
                ('Accomodation', models.TextField(blank=True, null=True)),
                ('practical', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'experience',
                'verbose_name_plural': 'experience',
            },
        ),
        migrations.CreateModel(
            name='ExperienceImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='uploads/images')),
                ('experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experience.Experience')),
            ],
            options={
                'verbose_name': 'experience Image',
                'verbose_name_plural': 'experience Images',
            },
        ),
    ]
