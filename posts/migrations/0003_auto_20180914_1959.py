# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-14 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20180914_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.CharField(max_length=255),
        ),
    ]
