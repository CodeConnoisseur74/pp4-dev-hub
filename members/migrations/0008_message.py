# Generated by Django 4.2.6 on 2023-11-23 19:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0007_rename_membername_profile_username"),
    ]

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                ("email", models.EmailField(blank=True, max_length=200, null=True)),
                ("subject", models.CharField(blank=True, max_length=200, null=True)),
                ("body", models.TextField()),
                ("is_read", models.BooleanField(default=False, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "recipient",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="messages",
                        to="members.profile",
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="members.profile",
                    ),
                ),
            ],
            options={
                "ordering": ["is_read", "-created"],
            },
        ),
    ]
