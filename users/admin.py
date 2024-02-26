from django.contrib import admin
from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "age", "can_be_contacted", "can_data_be_shared")


admin.site.register(User, UserAdmin)
