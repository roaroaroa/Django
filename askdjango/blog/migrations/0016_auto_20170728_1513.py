# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-28 06:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20170728_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=250),
        ),
    ]