# Generated by Django 4.1.5 on 2023-01-14 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_housechorerewardrequest_created_at"),
    ]

    operations = [
        migrations.RenameField(
            model_name="housechorerewardrequest",
            old_name="requester_acount",
            new_name="requester_account",
        ),
    ]