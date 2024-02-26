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

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from projects.models import Project, Issue, Comment
from projects.serializers import ProjectSerializer, IssueSerializer, CommentSerializer
from projects.permissions import IsAdminAuthenticated, IsAuthorOrReadOnly, IsContributoOrAuthorOrReadOnly


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

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class AdminIssuetViewset(ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAdminAuthenticated]

    def get_queryset(self):
        return Issue.objects.all()


class IssueViewset(ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsContributoOrAuthorOrReadOnly, IsAuthenticated]

    def get_queryset(self):
        return Issue.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class AdminCommentViewset(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsContributoOrAuthorOrReadOnly]

    def get_queryset(self):
        return Comment.objects.all()


class CommentViewset(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsContributoOrAuthorOrReadOnly, IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
