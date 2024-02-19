from rest_framework.serializers import ModelSerializer, ValidationError
from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'age', 'can_be_contacted', 'can_data_be_shared']

    def validate_age(self,age):
        if age <=15:
            raise ValidationError("Désolée vous n'avez pas l'âge requis." )
        return age
