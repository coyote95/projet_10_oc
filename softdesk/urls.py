from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users.views import UserViewset, SignupView

router = routers.DefaultRouter()
router.register(r'users', UserViewset)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('signup/', SignupView.as_view(), name='signup')
]
