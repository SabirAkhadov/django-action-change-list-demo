# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-09 09:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'Electronics', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='sale',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='testing.Category'),
        ),
    ]
