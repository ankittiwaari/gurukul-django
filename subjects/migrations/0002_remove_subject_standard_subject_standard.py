# Generated by Django 5.0.7 on 2025-03-04 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standards', '0003_alter_standard_title'),
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='standard',
        ),
        migrations.AddField(
            model_name='subject',
            name='standard',
            field=models.ManyToManyField(to='standards.standard'),
        ),
    ]
