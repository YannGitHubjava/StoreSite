# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothingStore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='Item', max_length=100, null=True),
        ),
    ]