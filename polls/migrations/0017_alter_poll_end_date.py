# Generated by Django 4.2 on 2023-12-04 09:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_alter_poll_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 11, 9, 24, 16, 773083, tzinfo=datetime.timezone.utc)),
        ),
    ]
