# Generated by Django 5.0.4 on 2024-05-13 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='corporate',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='free_time',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='my_skills',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='needed_skills',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='position',
        ),
    ]
