# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170202_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
