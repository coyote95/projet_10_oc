from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import status

from users.models import User
from users.serializers import UserSerializer


class AdminUserViewset(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        # Vérifier si le mot de passe est modifié
        password_modified = 'password' in serializer.validated_data and instance.password != serializer.validated_data[
            'password']

        # Effectuer la mise à jour
        self.perform_update(serializer)

        # Si le mot de passe est modifié, s'assurer qu'il reste haché
        if password_modified:
            instance.set_password(serializer.validated_data['password'])
            instance.save()

        return Response(serializer.data)




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
