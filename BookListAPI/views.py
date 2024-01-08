
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer


# Create your views here.

class showBooks (viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    ordering_fields=['rating','author']
    search_fields=['title', 'author', 'rating']


class newBook (generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class changeBook (generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
