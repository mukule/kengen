# Generated by Django 4.2 on 2023-04-26 08:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_alter_poll_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 3, 8, 13, 7, 712174, tzinfo=datetime.timezone.utc)),
        ),
    ]
