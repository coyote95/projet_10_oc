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
            return True

        # Check if the requesting user is the author of the object
        return obj.author == request.user


class IsContributorOrAuthorOrReadOnly(BasePermission):
    """
    Custom permission to only allow contributors, the author, or read-only access.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or request.method == "DELETE" or request.method == "PATCH":
            return self._is_contributor_or_author(request)

        if request.method == "POST":
            project_id = request.data.get("project")
            return project_id and (
                request.user == Project.objects.get(id=project_id).author
                or request.user in Project.objects.get(id=project_id).contributors.all()
            )

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return self._is_contributor_or_author(request, obj.project)

        return obj.author == request.user

    def _is_contributor_or_author(self, request, project=None):
        if project is None:
            return Project.objects.filter(Q(author=request.user) | Q(contributors=request.user)).exists()
        else:
            return request.user == project.author or request.user in project.contributors.all()
