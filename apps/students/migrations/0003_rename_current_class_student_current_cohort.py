# Generated by Django 4.2.2 on 2023-06-21 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0002_auto_20201124_0614"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student",
            old_name="current_class",
            new_name="current_cohort",
        ),
    ]
