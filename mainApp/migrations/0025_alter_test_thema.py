# Generated by Django 4.1.1 on 2022-11-15 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0024_alter_test_thema'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='thema',
            field=models.ForeignKey(blank=True, limit_choices_to=models.Q(('thema_set', 'subject_set')), null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.thema'),
        ),
    ]
