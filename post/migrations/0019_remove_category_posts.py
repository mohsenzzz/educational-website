# Generated by Django 4.2 on 2024-12-03 07:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0018_alter_category_posts_alter_post_categories"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="posts",
        ),
    ]
