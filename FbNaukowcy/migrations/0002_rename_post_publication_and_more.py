# Generated by Django 5.1.3 on 2024-11-16 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FbNaukowcy', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Publication',
        ),
        migrations.RenameField(
            model_name='publication',
            old_name='content',
            new_name='brief',
        ),
    ]