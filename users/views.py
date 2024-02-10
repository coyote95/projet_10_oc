from rest_framework.viewsets import ModelViewSet
from users.models import User
from users.serializers import UserSerializer
from users.forms import SignupForm
from django.views.generic.edit import CreateView
from django.conf import settings
from django.contrib.auth import login

class UserViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'signup.html'
    success_url = settings.LOGIN_REDIRECT_URL

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request,self.object)
        return response


