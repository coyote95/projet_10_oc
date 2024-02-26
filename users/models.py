"""
Module defining the 'User' model for the 'users' application.

Classes:
    - User(AbstractUser):
        Custom user model inheriting from Django's AbstractUser.

        Fields:
            - age: IntegerField representing the age of the user with validators to ensure a valid age range (0 to 150)
            - can_be_contacted: BooleanField indicating whether the user can be contacted
            - can_data_be_shared: BooleanField indicating whether the user is willing to share their data

        Methods:
            - __str__: Returns the username of the user when the object is converted to a string.
"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):
    age = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(150)])
    can_be_contacted = models.BooleanField(default=False, verbose_name="Peut-être contacté?")
    can_data_be_shared = models.BooleanField(default=False, verbose_name="Partager les données?")

    def __str__(self):
        return self.username
