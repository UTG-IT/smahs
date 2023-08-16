# Generated by Django 4.2.2 on 2023-08-14 12:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("staffs", "0011_remove_staff_role"),
        ("corecode", "0012_alter_course_lecturer"),
    ]

    operations = [
        migrations.CreateModel(
            name="Assignments",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                (
                    "date_created",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("due_date", models.DateTimeField(default=django.utils.timezone.now)),
                ("total_marks", models.IntegerField(default=0)),
                (
                    "academic_semester",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="corecode.academicsemester",
                    ),
                ),
                (
                    "academic_session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="corecode.academicsession",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="corecode.course",
                    ),
                ),
                (
                    "lecturer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="lecturer_assignment",
                        to="staffs.staff",
                    ),
                ),
            ],
            options={
                "ordering": ["-date_created"],
            },
        ),
    ]
