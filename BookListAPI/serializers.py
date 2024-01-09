from rest_framework import serializers
from .models import Book
from rest_framework.validators import UniqueValidator

#This serializer has some basic validation in the inputs taht only allows rating to be less than or equal to 5
#and for title to be a unique value 
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