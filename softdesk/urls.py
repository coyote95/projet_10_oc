from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from users.views import UserViewset, SignupView, UsersAPIView
from projects.views import ProjectAPIView, IssueAPIView, CommentAPIView


router = routers.DefaultRouter()
router.register(r'users', UserViewset)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('signup/', SignupView.as_view(), name='signup'),
    path('api/users/', UsersAPIView.as_view()),
    path('api/projects/', ProjectAPIView.as_view()),
    path('api/issues/', IssueAPIView.as_view()),
    path('api/comments/',CommentAPIView.as_view()),

]
