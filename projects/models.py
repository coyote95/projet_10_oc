from django.db import models
from users.models import User
import uuid


class Project(models.Model):
    BACKEND = 'BACKEND'
    FRONTEND = 'FRONTEND'
    IOS = 'IOS'
    ANDROID = 'ANDROID'

    TYPE_CHOICES = (
        (BACKEND, 'back-end'),
        (FRONTEND, 'front-end'),
        (IOS, 'ios'),
        (ANDROID, 'android')
    )
    name = models.CharField(max_length=100, verbose_name="titre")
    description = models.TextField(verbose_name="description")
    type = models.CharField(max_length=25, choices=TYPE_CHOICES)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    contributors = models.ManyToManyField(User, through='ProjectContributor', related_name='contributor')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProjectContributor(models.Model):
    contributor = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"contributor:{self.contributor}"


class Issue(models.Model):
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'

    PRIORITIES_CHOICES = (
        (LOW, 'low'),
        (MEDIUM, 'medium'),
        (HIGH, 'high')
    )

    BUG = 'BUG'
    FEATURE = 'FEATURE'
    TASK = 'TASK'

    TAGS_CHOICES = (
        (BUG, 'bug'),
        (FEATURE, 'feature'),
        (TASK, 'task')
    )

    TODO = 'TODO'
    INPROGRESS = 'INPROGRESS'
    FINISHED = 'FINISHED'

    STATUS_CHOICES = (
        (TODO, 'to do'),
        (INPROGRESS, 'in progress'),
        (TASK, 'task')
    )

    name = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    priority= models.CharField(max_length=25,choices=PRIORITIES_CHOICES)
    tag = models.CharField(max_length=25, choices=TAGS_CHOICES)
    status = models.CharField(max_length=25,choices=STATUS_CHOICES)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    created_time = models.DateTimeField(auto_now_add=True)