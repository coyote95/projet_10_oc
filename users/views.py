"""
File defining viewsets for the 'users' application using Django REST framework.

Classes:
    - AdminUserViewset(ModelViewSet):
        Viewset for administrative actions on User model. Requires admin authentication.
        Methods:
            - get_queryset: Returns all users.
            - update: Updates a user, checks for password modification, and ensures it remains hashed.

    - UserViewset(ModelViewSet):
        Viewset for basic actions on User model. Requires user authentication and restricts actions to
         the owner profile.

        Methods:
            - get_queryset: Returns users with can_data_be_shared set to True.
            - update: Updates a user, checks for password modification, and ensures it remains hashed.
"""

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from users.permissions import IsAdminAuthenticated, IsOwnerProfile

from users.models import User
from users.serializers import UserSerializer


class AdminUserViewset(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAdminAuthenticated]

    def get_queryset(self):
        return User.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        password_modified = (  # Check if the password is modified
            "password" in serializer.validated_data and instance.password != serializer.validated_data["password"]
        )
        self.perform_update(serializer)  # Perform the update
        if password_modified:  # If the password is modified, ensure it remains hashed
            instance.set_password(serializer.validated_data["password"])
            instance.save()

        return Response(serializer.data)


class UserViewset(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsOwnerProfile]

    def get_queryset(self):
        queryset = User.objects.filter(can_data_be_shared=True)

        # Check if the user is authenticated
        if self.request.user.is_authenticated:
            # Include the current user's profile in the queryset
            queryset |= User.objects.filter(id=self.request.user.id)

        return queryset

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        password_modified = (  # Check if the password is modified
            "password" in serializer.validated_data and instance.password != serializer.validated_data["password"]
        )
        self.perform_update(serializer)  # Perform the update
        if password_modified:  # If the password is modified, ensure it remains hashed
            instance.set_password(serializer.validated_data["password"])
            instance.save()

        return Response(serializer.data)
