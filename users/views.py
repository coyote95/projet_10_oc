from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from django.views.generic.edit import CreateView
from django.conf import settings
from django.contrib.auth import login

from users.models import User
from users.serializers import UserSerializer, UserSerializer2
from users.forms import SignupForm


class UserViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'signup.html'
    success_url = settings.LOGIN_REDIRECT_URL

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class UsersAPIView(APIView):
    def get(self, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer2(users, many=True)
        return Response(serializer.data)
