# Generated by Django 4.1.4 on 2023-01-04 04:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teacher', '0008_rename_notes_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='teacher',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]