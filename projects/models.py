"""
This file defines the Django models for the 'projects' application.

Classes:
    - Project(models.Model):
        A model representing a project.

        Fields:
            - name (CharField): The title of the project.
            - description (TextField): The description of the project.
            - type (CharField): The type of the project (backend, frontend, iOS, Android).
            - author (ForeignKey to User): The user who created the project.
            - contributors (ManyToManyField to User through ProjectContributor): The users contributing to the project.
            - created_time (DateTimeField): The timestamp when the project was created.

    - ProjectContributor(models.Model):
        A model representing the contributors to a project.

        Fields:
            - contributor (ForeignKey to User): The user contributing to the project.
            - project (ForeignKey to Project): The project to which the contributor is associated.

    - Issue(models.Model):
        A model representing an issue in a project.

        Fields:
            - name (CharField): The name of the issue.
            - description (TextField): The description of the issue.
            - project (ForeignKey to Project): The project to which the issue belongs.
            - author (ForeignKey to User): The user who created the issue.
            - priority (CharField): The priority level of the issue (low, medium, high).
            - tag (CharField): The tag indicating the type of issue (bug, feature, task).
            - status (CharField): The status of the issue (to do, in progress, task).
            - created_time (DateTimeField): The timestamp when the issue was created.

    - Comment(models.Model):
        A model representing a comment on an issue.

        Fields:
            - text (TextField): The text of the comment.
            - issue (ForeignKey to Issue): The issue to which the comment belongs.
            - author (ForeignKey to User): The user who created the comment.
            - uuid (UUIDField): A unique identifier for the comment.
            - created_time (DateTimeField): The timestamp when the comment was created.
"""

from django.db import models
from users.models import User
import uuid


class Project(models.Model):
    BACKEND = "BACKEND"
    FRONTEND = "FRONTEND"
    IOS = "IOS"
    ANDROID = "ANDROID"

    TYPE_CHOICES = ((BACKEND, "back-end"), (FRONTEND, "front-end"), (IOS, "ios"), (ANDROID, "android"))
    name = models.CharField(max_length=100, verbose_name="titre")
    description = models.TextField(verbose_name="description")
    type = models.CharField(max_length=25, choices=TYPE_CHOICES)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    contributors = models.ManyToManyField(User, through="ProjectContributor", related_name="contributor")
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProjectContributor(models.Model):
    contributor = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"contributor:{self.contributor}"


class Issue(models.Model):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

    PRIORITIES_CHOICES = ((LOW, "low"), (MEDIUM, "medium"), (HIGH, "high"))

    BUG = "BUG"
    FEATURE = "FEATURE"
    TASK = "TASK"

    TAGS_CHOICES = ((BUG, "bug"), (FEATURE, "feature"), (TASK, "task"))

    TODO = "TODO"
    INPROGRESS = "INPROGRESS"
    FINISHED = "FINISHED"

    STATUS_CHOICES = ((TODO, "to do"), (INPROGRESS, "in progress"), (TASK, "task"))

    name = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.CharField(max_length=25, choices=PRIORITIES_CHOICES)
    tag = models.CharField(max_length=25, choices=TAGS_CHOICES)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    created_time = models.DateTimeField(auto_now_add=True)
