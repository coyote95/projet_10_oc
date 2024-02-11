from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    age = models.IntegerField(default=0)
    can_be_contacted = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)

    def __str__(self):
        return self.username



