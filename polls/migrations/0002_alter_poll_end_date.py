# Generated by Django 4.1.7 on 2023-04-18 10:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 25, 10, 23, 42, 26083, tzinfo=datetime.timezone.utc)),
        ),
    ]
