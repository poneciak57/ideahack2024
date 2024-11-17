# Generated by Django 5.1.2 on 2024-11-17 00:26

import common.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_project_embedding'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='author',
            field=models.ForeignKey(default=common.models.Paper.get_default_author, on_delete=django.db.models.deletion.CASCADE, to='common.profile'),
        ),
    ]