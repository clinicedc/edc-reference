# Generated by Django 2.2.2 on 2019-07-14 21:03

from django.db import migrations
import django.db.models.manager
import edc_sites.models


class Migration(migrations.Migration):

    dependencies = [("edc_reference", "0008_auto_20190708_0605")]

    operations = [
        migrations.AlterModelManagers(
            name="reference",
            managers=[
                ("objects", django.db.models.manager.Manager()),
                ("on_site", edc_sites.models.CurrentSiteManager()),
            ],
        )
    ]
