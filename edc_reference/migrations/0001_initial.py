# Generated by Django 2.0 on 2017-12-13 20:34

import _socket
from django.db import migrations, models
import django_revision.revision_field
import edc_model_fields.fields.hostname_modification_field
import edc_model_fields.fields.userfield
import edc_model_fields.fields.uuid_auto_field
import edc_utils


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Reference",
            fields=[
                (
                    "created",
                    models.DateTimeField(blank=True, default=edc_utils.date.get_utcnow),
                ),
                (
                    "modified",
                    models.DateTimeField(blank=True, default=edc_utils.date.get_utcnow),
                ),
                (
                    "user_created",
                    edc_model_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    edc_model_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    edc_model_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    edc_model_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("identifier", models.CharField(max_length=50)),
                ("timepoint", models.CharField(max_length=50)),
                ("report_datetime", models.DateTimeField()),
                ("model", models.CharField(max_length=250)),
                ("field_name", models.CharField(max_length=50)),
                ("datatype", models.CharField(max_length=50)),
                ("value_str", models.CharField(max_length=50, null=True)),
                ("value_int", models.IntegerField(null=True)),
                ("value_date", models.DateField(null=True)),
                ("value_datetime", models.DateTimeField(null=True)),
            ],
            options={"ordering": ("identifier", "report_datetime")},
        ),
        migrations.AddIndex(
            model_name="reference",
            index=models.Index(
                fields=["identifier", "timepoint", "model"],
                name="edc_referen_identif_6df120_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="reference",
            index=models.Index(
                fields=["identifier", "report_datetime", "timepoint", "model"],
                name="edc_referen_identif_351847_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="reference",
            index=models.Index(
                fields=["report_datetime", "timepoint"],
                name="edc_referen_report__69deaa_idx",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="reference",
            unique_together={
                ("identifier", "timepoint", "report_datetime", "model", "field_name")
            },
        ),
    ]
