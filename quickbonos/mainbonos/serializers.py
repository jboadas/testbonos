from django.contrib.auth.models import User, Group
from rest_framework import serializers
from quickbonos.mainbonos.models import Bonos


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class BonosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bonos
        fields = ['bono_id', 'bono_name', 'bono_number', 'bono_price']
