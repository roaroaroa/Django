# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-24 16:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170725_0049'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rice_e',
            options={'ordering': ['-price']},
        ),
        migrations.AlterModelOptions(
            name='rice_l',
            options={'ordering': ['-price']},
        ),
        migrations.AlterModelOptions(
            name='tissue_e',
            options={'ordering': ['-price']},
        ),
        migrations.AlterModelOptions(
            name='tissue_l',
            options={'ordering': ['-price']},
        ),
        migrations.AlterModelOptions(
            name='water_e',
            options={'ordering': ['-price']},
        ),
        migrations.AlterModelOptions(
            name='water_l',
            options={'ordering': ['-price']},
        ),
    ]
