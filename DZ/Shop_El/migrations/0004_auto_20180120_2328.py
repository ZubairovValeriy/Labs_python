# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-20 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop_El', '0003_auto_20180120_2324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='users',
        ),
        migrations.AddField(
            model_name='profile',
            name='comps',
            field=models.ManyToManyField(to='Shop_El.Product'),
        ),
    ]
