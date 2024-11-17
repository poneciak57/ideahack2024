# Generated by Django 5.1.2 on 2024-11-17 04:39
from django.db import migrations
from datetime import date, timedelta

def add_finance_rounds_to_existing_projects(apps, schema_editor):
    Project = apps.get_model('common', 'Project')
    FinanceRound = apps.get_model('common', 'FinanceRound')

    # Define the project titles and their respective finance rounds
    finance_rounds = [
        {"project_title": "AI Startup", "title": "Seed Funding", "brief": "Initial seed round to kickstart operations.", "fundings_gathered": 500000, "end_date": date.today() + timedelta(days=60)},
        {"project_title": "Green Energy Initiative", "title": "Series A", "brief": "Expanding operations and hiring talent.", "fundings_gathered": 1000000, "end_date": date.today() + timedelta(days=120)},
        {"project_title": "Quantum Computing Research", "title": "Series B", "brief": "Scaling quantum computing infrastructure.", "fundings_gathered": 1500000, "end_date": date.today() + timedelta(days=180)},
        {"project_title": "Blockchain for Healthcare", "title": "Grant Funding", "brief": "Government grant for healthcare blockchain.", "fundings_gathered": 750000, "end_date": date.today() + timedelta(days=90)},
        {"project_title": "Biotech Innovations", "title": "Venture Capital Round", "brief": "Funding new biotech product development.", "fundings_gathered": 2000000, "end_date": date.today() + timedelta(days=150)},
    ]

    # Iterate through each finance round and associate it with the corresponding project
    for round_data in finance_rounds:
        try:
            project = Project.objects.get(title=round_data["project_title"])
            FinanceRound.objects.get_or_create(
                title=round_data["title"],
                project=project,
                defaults={
                    "brief": round_data["brief"],
                    "fundings_gathered": round_data["fundings_gathered"],
                    "end_date": round_data["end_date"],
                }
            )
        except Project.DoesNotExist:
            print(f"Project with title '{round_data['project_title']}' does not exist.")

def remove_finance_rounds_from_existing_projects(apps, schema_editor):
    FinanceRound = apps.get_model('common', 'FinanceRound')

    # Titles of finance rounds to remove
    finance_round_titles = [
        "Seed Funding",
        "Series A",
        "Series B",
        "Grant Funding",
        "Venture Capital Round",
    ]
    FinanceRound.objects.filter(title__in=finance_round_titles).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('common', '0010_merge_20241117_0512'),
    ]

    operations = [
        migrations.RunPython(add_finance_rounds_to_existing_projects, remove_finance_rounds_from_existing_projects),
    ]