from rest_framework import serializers
from .models import Book, PublicBook
from rest_framework.validators import UniqueValidator

#This serializer has some basic validation in the inputs that only allows rating to be less than or equal to 5
#and for title to be a unique value 
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'rating']
        extra_kwargs = {
            'rating': {
                'min_value': 0,
                'max_value': 5,
            },
            'title': {
                'validators': [UniqueValidator(queryset=Book.objects.all())]
            }
        }

# Serializer for PublicBook model
class PublicBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicBook
        fields = '__all__'
        extra_kwargs = {
            'rating': {
                'min_value': 0,
                'max_value': 5,
            },
            'title': {
                'validators': [UniqueValidator(queryset=PublicBook.objects.using('public_library').all())]
            }
        }

    def create(self, validated_data):
        return PublicBook.objects.using('public_library').create(**validated_data)