from rest_framework import serializers
from .models import Book
serializers.ValidationError,
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
