from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token 
User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    serializers.CharField()",
    "Token.objects.create", 
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        "get_user_model().objects.create_use
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
