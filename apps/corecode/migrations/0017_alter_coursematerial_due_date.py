# Generated by Django 4.2.2 on 2023-08-16 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("corecode", "0016_coursematerial_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coursematerial",
            name="due_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
