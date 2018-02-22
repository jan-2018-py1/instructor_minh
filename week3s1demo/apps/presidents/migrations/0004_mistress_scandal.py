# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-22 00:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('presidents', '0003_firstlady'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mistress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scandal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('mistress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scandals', to='presidents.Mistress')),
                ('president', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scandals', to='presidents.President')),
            ],
        ),
    ]
