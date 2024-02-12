from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from users.models import User


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'age', 'can_be_contacted',' can_data_be_shared ']


class UserSerializer2(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'age', 'can_be_contacted', 'can_data_be_shared' ]
