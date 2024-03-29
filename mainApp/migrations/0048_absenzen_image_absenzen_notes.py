# Generated by Django 4.1.1 on 2023-01-02 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0047_alter_thema_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='absenzen',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='absenzen/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='absenzen',
            name='notes',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
