from rest_framework.views import APIView
from rest_framework.response import Response

from projects.models import Project, Issue, Comment
from projects.serializers import ProjectSerializer, IssueSerializer, CommentSerializer


class ProjectAPIView(APIView):

    def get(self, *args, **kwargs):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class IssueAPIView(APIView):

    def get(self, *args, **kwargs):
        issues = Issue.objects.all()
        serializer = IssueSerializer(issues, many=True)
        return Response(serializer.data)


class CommentAPIView(APIView):

    def get(self, *args, **kwargs):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
