# Generated by Django 4.2 on 2024-11-29 13:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
        migrations.RemoveField(
            model_name="category",
            name="post",
        ),
        migrations.AddField(
            model_name="category",
            name="post",
            field=models.ManyToManyField(blank=True, null=True, to="post.post"),
        ),
    ]