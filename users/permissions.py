"""
File defining custom permissions for the 'users' application using Django REST framework.

Classes:
    - IsAdminAuthenticated(BasePermission):
        Custom permission class that allows access only to authenticated superusers.

    - IsOwnerProfile(BasePermission):
        Custom permission class that allows access only to the owner of the profile.
        Users must be authenticated to access this permission.
"""

from rest_framework.permissions import BasePermission


class IsAdminAuthenticated(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)


class IsOwnerProfile(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj == request.user
