# Generated by Django 4.1.1 on 2022-10-29 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0007_alter_schoolclass_options_alter_schoolclass_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schoolclass',
            options={'verbose_name': 'School Class', 'verbose_name_plural': 'es'},
        ),
    ]