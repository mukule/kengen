# Generated by Django 4.2 on 2023-04-25 10:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_poll_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 2, 10, 45, 37, 84165, tzinfo=datetime.timezone.utc)),
        ),
    ]
