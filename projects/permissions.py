from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated
from projects.models import Project


class IsAdminAuthenticated(BasePermission):

    def has_permission(self, request, view):
        # Ne donnons l’accès qu’aux utilisateurs administrateurs authentifiés
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)


class IsAuthorOrReadOnly(BasePermission):
    """
    Custom permission to only allow authors of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # If the request method is safe (GET, HEAD, OPTIONS), allow any access
        if request.method in SAFE_METHODS:
            return True

        # Check if the requesting user is the author of the object
        return obj.author == request.user


class IsContributoOrAuthorOrReadOnly(BasePermission):
    """
    Custom permission to only allow contributors or the author of the project associated with the issue to edit it.
    """

    def has_permission(self, request, view):
        # Si la méthode de requête est sécurisée (GET, HEAD, OPTIONS), permettre tout accès
        if request.method in SAFE_METHODS:
            return True

        # Vérifier si l'utilisateur demandeur est l'auteur du projet ou un contributeur du projet associé à l'issue
        if request.method == 'POST':
            project_id = request.data.get('project')  # Assurez-vous que le champ 'project' est inclus dans la requête
            return project_id and (
                    request.user == Project.objects.get(id=project_id).author
                    or request.user in Project.objects.get(id=project_id).contributors.all()
            )

    def has_object_permission(self, request, view, obj):
        # Si la méthode de requête est sécurisée (GET, HEAD, OPTIONS), permettre tout accès
        if request.method in SAFE_METHODS:
            return (
                    request.user == obj.project.author
                    or request.user in obj.project.contributors
            )

        return obj.author == request.user
