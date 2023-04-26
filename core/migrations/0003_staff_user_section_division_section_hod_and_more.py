# Generated by Django 4.2 on 2023-04-26 07:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_boardmember_division_section_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='section',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='core.division'),
        ),
        migrations.AddField(
            model_name='section',
            name='hod',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hod_section', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='division',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='divisions', to='core.department'),
        ),
        migrations.AddField(
            model_name='division',
            name='hod',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hod_division', to=settings.AUTH_USER_MODEL),
        ),
    ]
