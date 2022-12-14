# Generated by Django 4.1 on 2022-08-24 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0002_tag_scope"),
    ]

    operations = [
        migrations.AlterField(
            model_name="scope",
            name="article",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="scopes",
                to="articles.article",
            ),
        ),
        migrations.AlterField(
            model_name="scope",
            name="tag",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tags",
                to="articles.tag",
            ),
        ),
    ]
