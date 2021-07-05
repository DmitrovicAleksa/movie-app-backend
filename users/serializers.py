from django.contrib.auth import models
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    def validate_password(self,value):
        return make_password(value)

    class Meta:
        model = User
        fields = ['email','first_name','last_name','password']