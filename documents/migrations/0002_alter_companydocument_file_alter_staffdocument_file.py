# Generated by Django 4.1.7 on 2023-04-11 19:16

from django.db import migrations, models
import documents.models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydocument',
            name='file',
            field=models.FileField(upload_to='company_documents/', validators=[documents.models.validate_pdf]),
        ),
        migrations.AlterField(
            model_name='staffdocument',
            name='file',
            field=models.FileField(upload_to='staff_documents/', validators=[documents.models.validate_pdf]),
        ),
    ]
