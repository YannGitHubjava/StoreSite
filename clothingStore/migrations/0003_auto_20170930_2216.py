# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 22:16
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('clothingStore', '0002_product_name'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('pmg', django.db.models.manager.Manager()),
            ],
        ),
    ]
