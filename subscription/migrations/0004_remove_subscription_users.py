# Generated by Django 4.2 on 2024-12-04 17:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("subscription", "0003_subscription_description"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="subscription",
            name="users",
        ),
    ]
