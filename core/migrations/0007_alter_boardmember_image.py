# Generated by Django 4.2 on 2023-08-31 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_staff_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmember',
            name='image',
            field=models.ImageField(default='default/user.png', upload_to='board_members/'),
        ),
    ]
