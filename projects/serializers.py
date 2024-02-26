from rest_framework.serializers import ModelSerializer

from projects.models import Project, Issue, Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'issue', 'author', 'uuid', 'created_time']
        read_only_fields = ('author',)


class IssueSerializer(ModelSerializer):
    comments = CommentSerializer(many=True,required=False)

    class Meta:
        model = Issue
        fields = ['id', 'name', 'description', 'project', 'author', 'priority', 'tag', 'status', 'created_time',
                  'comments']
        read_only_fields = ('author',)


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'type', 'author','contributors', 'created_time']
        read_only_fields = ('author',)
