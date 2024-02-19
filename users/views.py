from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from django.views.generic.edit import CreateView
from django.conf import settings
from django.contrib.auth import login

from users.models import User
from users.serializers import UserSerializer
from users.forms import SignupForm


class AdminUserViewset(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()


class UserViewset(ReadOnlyModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

#
# class SignupView(CreateView):
#     form_class = SignupForm
#     template_name = 'signup.html'
#     success_url = settings.LOGIN_REDIRECT_URL
#
#     def form_valid(self, form):
#         response = super().form_valid(form)
#         login(self.request, self.object)
#         return response
