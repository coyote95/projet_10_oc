from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):
    age = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(150)])
    can_be_contacted = models.BooleanField(default=False, verbose_name='Peut-être contacté?')
    can_data_be_shared = models.BooleanField(default=False, verbose_name='Partager les données?')

    def __str__(self):
        return self.username
