# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20170725_2032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rice', models.BooleanField(default=False)),
                ('water', models.BooleanField(default=False)),
                ('tissue', models.BooleanField(default=False)),
            ],
        ),
    ]
