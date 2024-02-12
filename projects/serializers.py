from rest_framework.serializers import ModelSerializer

from projects.models import Project, Issue, Comment


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'description', 'type', 'author', 'contributors', 'created_time']


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = ['name', 'description', 'project', 'author', 'priority', 'tag', 'status', 'created_time']


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text', 'issue', 'author', 'uuid', 'created_time']
