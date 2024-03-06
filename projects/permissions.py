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
from django.db.models import Q

from projects.models import Project, Issue


class IsAdminAuthenticated(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)


class IsAuthorOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        # If the request method is safe (GET, HEAD, OPTIONS), allow full access
        if request.method in SAFE_METHODS:
            print("permission auteur: obj all")
            return True
        print("permission auteur: obj author")
        # Check if the requesting user is the author of the object
        return obj.author == request.user


class IsProjectAuthorOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        print("autheur")
        project_id = request.data.get("project")
        if not project_id:
            return Project.objects.filter(author=request.user).exists()
        try:
            # Get the project instance based on the provided project_id
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            return False

        return request.user == project.author

    # def has_object_permission(self, request, view, obj):
    #     print("autheur obj")
    #     return obj.author == request.user


class IsProjectContributor(BasePermission):
    def has_permission(self, request, view):
        print("contributor")
        project_id = request.data.get("project")
        if not project_id:
            return Project.objects.filter(contributors=request.user).exists()
        try:
            # Get the project instance based on the provided project_id
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            return False

        return request.user in project.contributors.all()

    # def has_object_permission(self, request, view, obj):
    #     print("bof")
    #     return obj.author == request.user
