# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-06 21:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20160406_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='id_categoria',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='id_proveedor',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
