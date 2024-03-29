# Generated by Django 3.2.5 on 2024-02-11 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, verbose_name="titre")),
                ("description", models.TextField(verbose_name="description")),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("BACKEND", "back-end"),
                            ("FRONTEND", "front-end"),
                            ("IOS", "ios"),
                            ("ANDROID", "android"),
                        ],
                        max_length=25,
                    ),
                ),
                ("created_time", models.DateTimeField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="author", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProjectContributor",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "contributor",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
                ("project", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="projects.project")),
            ],
        ),
        migrations.AddField(
            model_name="project",
            name="contributors",
            field=models.ManyToManyField(
                related_name="contributor", through="projects.ProjectContributor", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.CreateModel(
            name="Issue",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "priority",
                    models.CharField(choices=[("LOW", "low"), ("MEDIUM", "medium"), ("HIGH", "high")], max_length=25),
                ),
                (
                    "tag",
                    models.CharField(
                        choices=[("BUG", "bug"), ("FEATURE", "feature"), ("TASK", "task")], max_length=25
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("TODO", "to do"), ("INPROGRESS", "in progress"), ("TASK", "task")], max_length=25
                    ),
                ),
                ("created_time", models.DateTimeField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
                ("project", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="projects.project")),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("text", models.TextField()),
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("created_time", models.DateTimeField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
                ("issue", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="projects.issue")),
            ],
        ),
    ]
