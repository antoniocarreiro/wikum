# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-18 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_comment_num_subchildren'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='vector',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]