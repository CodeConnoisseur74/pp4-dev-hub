# Generated by Django 4.2.6 on 2023-11-05 17:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0002_alter_profile_options_skill"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="social_youtube",
            new_name="social_stackoverflow",
        ),
    ]
