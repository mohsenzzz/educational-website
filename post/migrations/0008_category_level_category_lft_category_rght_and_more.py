# Generated by Django 4.2 on 2024-12-01 13:14

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0007_post_categories_alter_category_parent"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="level",
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="category",
            name="lft",
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="category",
            name="rght",
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="category",
            name="tree_id",
            field=models.PositiveIntegerField(
                db_index=True, default=None, editable=False
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="category",
            name="parent",
            field=mptt.fields.TreeForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="children",
                to="post.category",
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="posts",
            field=models.ManyToManyField(to="post.post"),
        ),
        migrations.AlterField(
            model_name="post",
            name="categories",
            field=models.ManyToManyField(to="post.category"),
        ),
    ]
