# Generated by Django 4.2 on 2023-12-04 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_department_performance_score_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='vision',
            field=models.TextField(blank=True, null=True),
        ),
    ]