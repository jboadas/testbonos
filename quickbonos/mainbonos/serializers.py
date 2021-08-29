from django.contrib.auth.models import User
from rest_framework import serializers
from quickbonos.mainbonos.models import Bonos


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class BonosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bonos
        fields = '__all__'

    def create(self, validated_data):
        bono = super().create(validated_data)
        bono.created_by = self.context['request'].user
        bono.save()
        return bono
