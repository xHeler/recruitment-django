# Generated by Django 4.1.7 on 2023-03-09 10:26

import uuid

import django.core.validators
import django.db.models.deletion
import sorl.thumbnail.fields
from django.conf import settings
from django.db import migrations, models

import src.images.utils


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Thumbnail",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "image",
                    sorl.thumbnail.fields.ImageField(
                        upload_to=src.images.utils.file_generate_upload_path,
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["png", "jpg"]
                            )
                        ],
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "uploaded_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
