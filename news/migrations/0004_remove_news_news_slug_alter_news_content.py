# Generated by Django 4.1.7 on 2023-04-03 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_news_news_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='news_slug',
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(),
        ),
    ]
