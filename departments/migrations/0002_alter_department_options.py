# Generated by Django 5.0.7 on 2025-02-28 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['title'], 'verbose_name_plural': 'Departments'},
        ),
    ]
