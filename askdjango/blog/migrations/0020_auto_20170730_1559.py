# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-30 06:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20170728_2038'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Discount',
        ),
        migrations.DeleteModel(
            name='Emart',
        ),
        migrations.DeleteModel(
            name='Handling',
        ),
        migrations.DeleteModel(
            name='Handling2',
        ),
        migrations.DeleteModel(
            name='Handling3',
        ),
        migrations.DeleteModel(
            name='Scrapping',
        ),
    ]
