# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170202_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='body',
            field=models.TextField(null=True),
        ),
    ]