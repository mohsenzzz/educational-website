# Generated by Django 4.2 on 2024-12-03 06:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0008_category_level_category_lft_category_rght_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="slug",
            field=models.SlugField(default=None, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
