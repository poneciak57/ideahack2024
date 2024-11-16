# Generated by Django 5.1.3 on 2024-11-16 21:06

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('brief', models.TextField()),
                ('link', models.CharField(max_length=100)),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('embedding', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), blank=True, default=list, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('open_for_contact', models.BooleanField(default=True)),
            ],
        ),
    ]
