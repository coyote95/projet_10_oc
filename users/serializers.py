from rest_framework.serializers import ModelSerializer, ValidationError
from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'age', 'can_be_contacted', 'can_data_be_shared']

    def validate_age(self, age):
        if age <= 15:
            raise ValidationError("Désolée vous n'avez pas l'âge requis.")
        return age

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        if not password or len(password) < 8:
            raise ValidationError("Le mot de passe doit avoir au moins 8 caractères.")

        user = User.objects.create_user(**validated_data,password=password)
        return user


