# Generated by Django 4.1.1 on 2022-11-16 13:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0029_alter_test_thema'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='grade',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)]),
        ),
        migrations.AlterField(
            model_name='test',
            name='thema',
            field=models.ForeignKey(blank=True, limit_choices_to=models.Q('subject'), null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.thema'),
        ),
    ]
