# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-07 01:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(choices=[('save', 'Guardardo'), ('update', 'Modifico'), ('delete', 'Elimino'), ('buy', 'Compro'), ('check', 'Consulto')], max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BitacoraCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(max_length=100)),
                ('id_accion', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cliente.Accion')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cliente.Cliente')),
            ],
        ),
    ]
