# Generated by Django 4.1.7 on 2023-04-04 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='members',
        ),
    ]
