# Generated by Django 4.1.4 on 2023-01-03 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_trimester', models.IntegerField()),
                ('second_trimester', models.IntegerField()),
                ('third_trimester', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.subject')),
            ],
        ),
    ]