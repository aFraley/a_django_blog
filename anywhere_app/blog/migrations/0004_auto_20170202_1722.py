# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(null=True),
        ),
    ]
