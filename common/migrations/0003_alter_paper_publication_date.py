# Generated by Django 5.1.3 on 2024-11-16 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_paper'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='publication_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]