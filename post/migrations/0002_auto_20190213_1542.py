# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-13 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(),
        ),
    ]
