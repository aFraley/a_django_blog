# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 18:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170202_1812'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='topic',
        ),
    ]