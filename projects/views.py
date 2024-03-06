"""
Module defining viewsets for the 'projects' application using Django REST framework.

Classes:
    - AdminProjectViewset(ModelViewSet):
        Viewset for administrative actions on Project model. Requires admin authentication.

    - ProjectViewset(ModelViewSet):
        Viewset for basic actions on Project model. Requires user authentication and restricts actions to the author.

    - AdminIssuetViewset(ModelViewSet):
        Viewset for administrative actions on Issue model. Requires admin authentication.

    - IssueViewset(ModelViewSet):
        Viewset for basic actions on Issue model. Requires user authentication and restricts actions
         to contributors or authors.

    - AdminCommentViewset(ModelViewSet):
        Viewset for administrative actions on Comment model. Requires admin authentication.

    - CommentViewset(ModelViewSet):
        Viewset for basic actions on Comment model. Requires user authentication and restricts actions
         to contributors or authors.
"""

from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from projects.models import Project, Issue, Comment
from users.models import User
from projects.serializers import ProjectSerializer, IssueSerializer, CommentSerializer
from projects.permissions import IsAdminAuthenticated, IsAuthorOrReadOnly, IsProjectContributor, \
    IsProjectAuthor
from django.db.models import Q


class AdminProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminAuthenticated]

    def get_queryset(self):
        return Project.objects.all()


class ProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        queryset = Project.objects.all()
        project_id = self.request.GET.get("project_id")
        if project_id is not None:
            queryset = queryset.filter(id=project_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=["post"])
    def add_contributor(self, request, pk=None):
        project = self.get_object()
        contributor_id = request.data.get("contributor")  # Assuming the contributor ID is sent in the request data
        if contributor_id is not None:
            try:
                contributor = User.objects.get(pk=contributor_id)
                project.contributors.add(contributor)
                project.save()
                return Response({"detail": "Contributor added successfully."})
            except User.DoesNotExist:
                return Response({"detail": "Contributor not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(
                {"detail": "Contributor ID not provided in the request data."}, status=status.HTTP_400_BAD_REQUEST
            )

    @action(detail=True, methods=["post"])
    def del_contributor(self, request, pk=None):
        project = self.get_object()
        contributor_id = request.data.get("contributor")  # Assuming the contributor ID is sent in the request data
        if contributor_id is not None:
            try:
                contributor = User.objects.get(pk=contributor_id)
                project.contributors.remove(contributor)
                project.save()
                return Response({"detail": "Contributor removed successfully."})
            except User.DoesNotExist:
                return Response({"detail": "Contributor not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(
                {"detail": "Contributor ID not provided in the request data."}, status=status.HTTP_400_BAD_REQUEST
            )


class AdminIssuetViewset(ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAdminAuthenticated]

    def get_queryset(self):
        return Issue.objects.all()


class IssueViewset(ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthorOrReadOnly, IsProjectAuthor| IsProjectContributor]

    def get_queryset(self):
        return Issue.objects.filter(Q(project__author=self.request.user) | Q(project__contributors=self.request.user))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AdminCommentViewset(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAdminAuthenticated]

    def get_queryset(self):
        return Comment.objects.all()


class CommentViewset(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly, IsProjectAuthor | IsProjectContributor]

    def get_queryset(self):
        return Comment.objects.filter(
            Q(issue__project__author=self.request.user) | Q(issue__project__contributors=self.request.user))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
