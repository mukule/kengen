# Generated by Django 4.2 on 2023-04-26 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_staff_last_performance_review_staff_awards_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='staff_members', to='core.section'),
        ),
    ]