from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response

from projects.models import Project, Issue, Comment
from projects.serializers import ProjectSerializer, IssueSerializer, CommentSerializer


class AdminProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()


class ProjectViewset(ReadOnlyModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = Project.objects.all()
        project_id = self.request.GET.get('project_id')
        if project_id is not None:
            queryset = queryset.filter(id=project_id)
        return queryset


class AdminIssuetViewset(ModelViewSet):
    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.all()


class IssueViewset(ReadOnlyModelViewSet):
    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.all()


class AdminCommentViewset(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()


class CommentViewset(ReadOnlyModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()
