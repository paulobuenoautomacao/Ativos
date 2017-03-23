# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 22:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_auto_20170323_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100, verbose_name='Modelo')),
                ('patrimony', models.CharField(blank=True, max_length=20, verbose_name='Patrimônio')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'verbose_name': 'Equipamento',
                'verbose_name_plural': 'Equipamentos',
                'ordering': ['equipment'],
            },
        ),
        migrations.CreateModel(
            name='AssetType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4, verbose_name='Código')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'verbose_name': 'Tipo de Ativo',
                'verbose_name_plural': 'Tipos de Ativos',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Manufacturer', verbose_name='Fabricante')),
            ],
            options={
                'verbose_name': 'Reparo',
                'verbose_name_plural': 'Reparos',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('tag', models.CharField(max_length=50, verbose_name='TAG')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.Asset', verbose_name='Equipamento')),
            ],
            options={
                'verbose_name': 'TAG',
                'verbose_name_plural': 'TAGs',
                'ordering': ['tag'],
            },
        ),
        migrations.AddField(
            model_name='asset',
            name='assetType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='asset.AssetType', verbose_name='Tipo de ativo'),
        ),
        migrations.AddField(
            model_name='asset',
            name='equipment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Equipment', verbose_name='Equipamento'),
        ),
        migrations.AddField(
            model_name='asset',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Manufacturer', verbose_name='Fabricante'),
        ),
        migrations.AddField(
            model_name='asset',
            name='repair',
            field=models.ManyToManyField(blank=True, to='asset.Repair', verbose_name='Reparos'),
        ),
    ]
