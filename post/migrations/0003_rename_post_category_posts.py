# Generated by Django 4.2 on 2024-11-29 13:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0002_alter_category_options_remove_category_post_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="category",
            old_name="post",
            new_name="posts",
        ),
    ]