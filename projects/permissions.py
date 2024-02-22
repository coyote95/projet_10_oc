from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated


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


