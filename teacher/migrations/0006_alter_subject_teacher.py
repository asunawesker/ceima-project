# Generated by Django 4.1.4 on 2023-01-04 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0005_alter_subject_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='teacher',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]