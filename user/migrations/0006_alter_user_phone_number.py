# Generated by Django 4.2 on 2024-11-29 13:09

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0005_alter_user_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                default="09333333333", max_length=128, region=None, unique=True
            ),
        ),
    ]
