# Generated by Django 5.1.3 on 2024-11-16 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_remove_paper_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
