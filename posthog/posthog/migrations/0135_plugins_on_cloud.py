# Generated by Django 3.0.11 on 2021-03-19 13:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posthog", "0134_event_site_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organization",
            name="plugins_access_level",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "none"), (3, "config"), (6, "install"), (9, "root")],
                default=3 if settings.MULTI_TENANCY else 9,
            ),
        ),
    ]
