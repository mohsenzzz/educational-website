# Generated by Django 4.2 on 2024-12-03 06:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0009_category_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
    ]
