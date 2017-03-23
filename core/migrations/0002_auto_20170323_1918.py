# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 22:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='subsidiary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Subsidiary', verbose_name='Unidade'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Department', verbose_name='Departamento'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='local',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Local', verbose_name='Local'),
        ),
        migrations.AlterField(
            model_name='local',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Department', verbose_name='Departamento'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Company', verbose_name='Compania'),
        ),
        migrations.AlterField(
            model_name='subsidiary',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Company', verbose_name='Compania'),
        ),
    ]
