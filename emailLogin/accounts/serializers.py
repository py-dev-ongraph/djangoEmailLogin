from rest_framework import serializers
from accounts.models import User
from rest_auth.models import TokenModel

from rest_auth.serializers import LoginSerializer, TokenSerializer, UserDetailsSerializer


class CustomLoginResponseSerializer(serializers.ModelSerializer):
    """
    custom serializer to return all relevant user data on hitting login api
    """
    email = serializers.CharField(source='user.email')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    is_staff = serializers.CharField(source='user.is_staff')
    class Meta:
        model = TokenModel
        fields = ('email', 'key', 'first_name', 'last_name', 'is_staff', )