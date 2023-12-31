# Generated by Django 4.2.6 on 2023-11-03 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0001_initial"),
        ("projects", "0005_alter_project_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="members.profile",
            ),
        ),
    ]
