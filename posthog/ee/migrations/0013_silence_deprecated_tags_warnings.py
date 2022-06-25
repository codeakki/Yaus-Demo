# Generated by Django 3.2.13 on 2022-06-23 16:11

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ee", "0012_migrate_tags_v2"),
    ]

    operations = [
        migrations.RenameField(model_name="enterpriseeventdefinition", old_name="tags", new_name="deprecated_tags_v2",),
        migrations.RenameField(
            model_name="enterprisepropertydefinition", old_name="tags", new_name="deprecated_tags_v2",
        ),
        migrations.AlterField(
            model_name="enterpriseeventdefinition",
            name="deprecated_tags_v2",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=32),
                blank=True,
                db_column="tags",
                default=None,
                null=True,
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="enterprisepropertydefinition",
            name="deprecated_tags_v2",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=32),
                blank=True,
                db_column="tags",
                default=None,
                null=True,
                size=None,
            ),
        ),
    ]
