# Generated by Django 2.1.1 on 2019-10-29 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0057_auto_20190428_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_locked',
            field=models.BooleanField(default=False),
        ),
    ]
