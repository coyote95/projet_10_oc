"""
File defining the Django admin configuration for the 'User' model in the 'users' application.

Classes:
    - UserAdmin(admin.ModelAdmin):
        Custom admin configuration for the User model.

        Attributes:
            - list_display: List of fields to display in the list of users, including username, age,
              can_be_contacted, and can_data_be_shared.
"""

from django.contrib import admin
from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "age", "can_be_contacted", "can_data_be_shared")


admin.site.register(User, UserAdmin)
