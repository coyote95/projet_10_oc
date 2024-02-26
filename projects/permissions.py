"""
File defining custom permissions for the 'projects' application using Django REST framework.

Classes:
    - IsAdminAuthenticated(BasePermission):
        Custom permission class that allows access only to authenticated superusers.

    - IsAuthorOrReadOnly(BasePermission):
        Custom permission class that allows full access for safe methods (GET, HEAD, OPTIONS)
        and restricts modification to the author of the object.

    - IsContributoOrAuthorOrReadOnly(BasePermission):
        Custom permission class that allows full access for safe methods (GET, HEAD, OPTIONS),
        allows the creation of objects if the user is the author or a contributor of the project,
        and restricts modification to the author or contributors of the object.
"""

from rest_framework.permissions import BasePermission, SAFE_METHODS
from projects.models import Project


class IsAdminAuthenticated(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)


class IsAuthorOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        # If the request method is safe (GET, HEAD, OPTIONS), allow full access
        if request.method in SAFE_METHODS:
            return True

        # Check if the requesting user is the author of the object
        return obj.author == request.user


class IsContributoOrAuthorOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        # If the request method is safe (GET, HEAD, OPTIONS), allow full access
        if request.method in SAFE_METHODS:
            return True

        if request.method == "POST":
            project_id = request.data.get("project")
            return project_id and (
                request.user == Project.objects.get(id=project_id).author
                or request.user in Project.objects.get(id=project_id).contributors.all()
            )

    def has_object_permission(self, request, view, obj):
        # If the request method is safe (GET, HEAD, OPTIONS), allow full access
        if request.method in SAFE_METHODS:
            return request.user == obj.project.author or request.user in obj.project.contributors

        return obj.author == request.user
