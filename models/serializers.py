from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class Service_Sections_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Service_Section_Model
        fields = '__all__'

class Service_Serializer(serializers.ModelSerializer):
    sections = Service_Sections_Serializer(many=True, read_only=True)
    class Meta:
        model = Service_Model
        fields = '__all__'


class Contact_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Contact_Model
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user