# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 08:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pcol1', models.CharField(max_length=50)),
                ('Pcol2', models.CharField(max_length=10)),
                ('Pcol3', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Scol2', models.CharField(max_length=30)),
                ('Scol3', models.CharField(max_length=10)),
                ('Scol1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FirstApp.Pri')),
            ],
        ),
    ]
