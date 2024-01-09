
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from django.shortcuts import render

# Create your views here.

#Is a get that allows to look at books in the library. Allows filtering, sorting and searching.
class showBooks (viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    ordering_fields=['rating','author']
    search_fields=['title', 'author', 'rating']

#Allows to add Books to my library
class newBook (generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#Allows to change/delete books in the database 
class changeBook (generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#This connects to the index.html
def index(request):
    return render(request, 'index.html', {})

#Connects to library.html
def ListshowBooks(request):
    data = Book.objects.all()
    context = {"book": data}
    return render(request, "library.html", context)