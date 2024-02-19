from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from users.views import UserViewset, SignupView, UsersAPIView
from projects.views import ProjectViewset, IssueViewset, CommentViewset, AdminProjectViewset, AdminIssuetViewset, AdminCommentViewset


router = routers.SimpleRouter()

router.register(r'users', UserViewset)
router.register('projects',ProjectViewset, basename='projects')
router.register('issues',IssueViewset,basename='issues')
router.register('comments',CommentViewset,basename='comments')

router.register('admin/projects', AdminProjectViewset, basename='admin-projects')
router.register('admin/issues', AdminIssuetViewset, basename='admin-issues')
router.register('admin/comments', AdminCommentViewset, basename='admin-comments')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('signup/', SignupView.as_view(), name='signup'),
    path('api/users/', UsersAPIView.as_view()),
    path('api/',include(router.urls))
]
