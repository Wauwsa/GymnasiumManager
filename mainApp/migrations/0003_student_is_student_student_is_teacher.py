# Generated by Django 4.1.1 on 2022-10-29 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_absenzen'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_student',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='is_teacher',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
