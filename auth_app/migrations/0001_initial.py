# Generated by Django 5.1.2 on 2024-11-16 19:12

from django.db import migrations

def add_example_users(apps, schema_editor):
    User = apps.get_model('auth', 'User')  # Use the User model from auth
    User.objects.create_superuser(
        username='biznes_user',
        email='biznes@example.com',
        password='biznes_user'
    )
    User.objects.create_superuser(
        username='nauka_user',
        email='nauka@example.com',
        password='nauka_user'
    )
    User.objects.create_superuser(
        username='invest_user',
        email='invest@example.com',
        password='invest_user'
    )

def remove_example_users(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.filter(username='biznes_user').delete()
    User.objects.filter(username='nauka_user').delete()
    User.objects.filter(username='invest_user').delete()

class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'), 
    ]

    operations = [
        migrations.RunPython(add_example_users, remove_example_users),
    ]