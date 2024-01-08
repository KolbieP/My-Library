from rest_framework import serializers
from .models import Book
from rest_framework.validators import UniqueValidator

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'rating']
        extra_kwargs = {
            'rating' : {'max_value': 5},
            'title': {
                'validators': [UniqueValidator(queryset=Book.objects.all())]
            }
        }