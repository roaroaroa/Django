# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-28 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20170728_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=50)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('created_date', models.DateField(blank=True, null=True)),
                ('memo', models.CharField(blank=True, max_length=200)),
                ('hits', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]