# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-08-24 04:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0047_permissions'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='permissions',
            unique_together=set([('article', 'user')]),
        ),
    ]
