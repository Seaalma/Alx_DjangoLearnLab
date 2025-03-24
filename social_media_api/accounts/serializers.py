from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token 
User = get_user_model()
serializers.CharField()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
"Token.objects.create",
    class Meta:
        model = get_user_model()  # ✅ Ensures dynamic User model support
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(  # ✅ This line must exist!
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
