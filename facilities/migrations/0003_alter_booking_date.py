# Generated by Django 4.1.7 on 2023-04-13 15:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', '0002_booking_date_alter_booking_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]