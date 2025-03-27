from rest_framework import generics, viewsets
from .models import Book, PublicBook
from .serializers import BookSerializer
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

#Is a Class-based view that allows to look at books in the library. Allows filtering, sorting and searching. - GET
class showBooks (viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    ordering_fields=['rating','author']
    search_fields=['title', 'author', 'rating']

#Allows to add Books to my library - POST
class newBook (generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#Allows to change/delete books in the database - DELETE
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


#Allows search function to search the database
def search_books(request):
    query = request.GET.get('query', '')
    if query:
        books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
    else:
        books = Book.objects.all()
    
    results = [{'title': book.title, 'author': book.author, 'rating': book.rating} for book in books]
    return JsonResponse(results, safe=False)


def add_public_book(request):
    # Add book to public library
    PublicBook.objects.using('public_library').create(title="New Book", author="Author", rating=5)