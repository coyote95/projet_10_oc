"""
File defining custom permissions for the 'projects' application using Django REST framework.

Classes:
    - IsAdminAuthenticated(BasePermission):
        Custom permission class that allows access only to authenticated superusers.

    - IsAuthorOrReadOnly(BasePermission):
        Custom permission class that allows full access for safe methods (GET, HEAD, OPTIONS)
        and restricts modification to the author of the object.

    - IsProjectAuthor(BasePermission):
        Custom permission class that allows access only to the author of the specified project.

    - IsProjectContributor(BasePermission):
        Custom permission class that allows access only to contributors of the specified project.
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


class IsProjectAuthor(BasePermission):

    def has_permission(self, request, view):
        project_id = request.data.get("project")
        if not project_id:
            return Project.objects.filter(author=request.user).exists()
        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            return False

        return request.user == project.author


class IsProjectContributor(BasePermission):

    def has_permission(self, request, view):
        project_id = request.data.get("project")
        if not project_id:
            return Project.objects.filter(contributors=request.user).exists()
        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            return False

        return request.user in project.contributors.all()


