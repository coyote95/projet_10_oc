"""
File defining a serializer for the 'User' model in the 'users' application using Django REST framework.

Classes:
    - UserSerializer(ModelSerializer):
        Fields: "id", "username", "password", "age", "can_be_contacted", "can_data_be_shared".

        Methods:
            - validate_age: Custom validation method for the 'age' field, ensuring users are at least 16 years old.
            - create: Custom creation method to handle password validation and create a new user instance.
"""

from rest_framework.serializers import ModelSerializer, ValidationError
from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "age", "can_be_contacted", "can_data_be_shared"]

    def validate_age(self, age):
        if age <= 15:
            raise ValidationError("Désolée vous n'avez pas l'âge requis.")
        return age

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        if not password or len(password) < 8:
            raise ValidationError("Le mot de passe doit avoir au moins 8 caractères.")

        user = User.objects.create_user(**validated_data, password=password)
        return user
