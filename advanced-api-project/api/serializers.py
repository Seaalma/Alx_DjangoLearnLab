from rest_framework import serializers
from .models import Book
class AuthorSerializer(serializers.ModelSerializer), 
(many=True, read_only=True)
serializers.ValidationError,
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
