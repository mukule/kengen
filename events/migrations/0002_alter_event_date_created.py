# Generated by Django 4.1.7 on 2023-04-06 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
