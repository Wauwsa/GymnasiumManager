# Generated by Django 4.1.4 on 2022-12-31 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0041_alter_person_klasse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='klasse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.schoolclass'),
        ),
    ]
