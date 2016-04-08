# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-07 02:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_personaladministrativo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaladministrativo',
            name='foto',
            field=models.ImageField(blank=True, default='img_personal/no-img.jpg', upload_to='img_personal'),
        ),
        migrations.AlterField(
            model_name='personaladministrativo',
            name='id_permiso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='login.Permiso'),
        ),
    ]