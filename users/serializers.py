from django.contrib.auth import models
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    def validate_password(self,value):
        return make_password(value)
    
    def create(self, validated_data):

        user = User.objects.create_user(
            email=validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            password=validated_data['password'],
        )
        return user

    class Meta:
        model = User
        fields = ['email','first_name','last_name','password']