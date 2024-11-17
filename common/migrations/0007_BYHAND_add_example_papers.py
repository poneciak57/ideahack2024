# Generated by Django 5.1.3 on 2024-11-17 00:31

from django.db import migrations

def add_example_papers(apps, schema_editor):
    Paper = apps.get_model('common', 'Paper')
    Profile = apps.get_model('common', 'Profile')

    # Assuming we have at least one profile to associate with the papers
    author = Profile.objects.first()

    papers = [
        {
            "title": "The Future of AI",
            "brief": "An in-depth look at the advancements and future prospects of artificial intelligence.",
            "link": "http://example.com/future-of-ai",
        },
        {
            "title": "Quantum Computing Explained",
            "brief": "A comprehensive guide to understanding quantum computing and its potential applications.",
            "link": "http://example.com/quantum-computing",
        },
        {
            "title": "Renewable Energy Sources",
            "brief": "An analysis of various renewable energy sources and their impact on the environment.",
            "link": "http://example.com/renewable-energy",
        },
        {
            "title": "Blockchain Technology",
            "brief": "Exploring the fundamentals of blockchain technology and its use cases beyond cryptocurrencies.",
            "link": "http://example.com/blockchain-technology",
        },
        {
            "title": "Advancements in Biotechnology",
            "brief": "A review of recent advancements in biotechnology and their implications for healthcare.",
            "link": "http://example.com/biotechnology",
        },
    ]

    for paper_data in papers:
        Paper.objects.create(
            author=author,
            title=paper_data["title"],
            brief=paper_data["brief"],
            link=paper_data["link"],
        )

def remove_example_papers(apps, schema_editor):
    Paper = apps.get_model('common', 'Paper')
    Paper.objects.filter(
        title__in=[
            "The Future of AI",
            "Quantum Computing Explained",
            "Renewable Energy Sources",
            "Blockchain Technology",
            "Advancements in Biotechnology",
        ]
    ).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_BYHAND_add_first_last_names'),
    ]

    operations = [
        migrations.RunPython(add_example_papers, remove_example_papers),
    ]