# Generated by Django 4.1.1 on 2022-12-28 15:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0044_thema_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thema',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 28, 16, 1, 10, 504470)),
        ),
    ]
