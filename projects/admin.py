from django.contrib import admin
from projects.models import Project, Issue, Comment, ProjectContributor


class ProjectContributorInline(admin.TabularInline):
    model = ProjectContributor


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "type", "author", "created_time", "display_contributors")
    inlines = [ProjectContributorInline]

    def display_contributors(self, obj):
        return ", ".join([contributor.username for contributor in obj.contributors.all()])


class IssueAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "project", "author", "priority", "tag", "status", "created_time")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("text", "issue", "author", "uuid", "created_time")


class ProjectContributorAdmin(admin.ModelAdmin):
    list_display = ("contributor", "project")


admin.site.register(Project, ProjectAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(ProjectContributor, ProjectContributorAdmin)
