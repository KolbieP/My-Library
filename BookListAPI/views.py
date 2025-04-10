from rest_framework import generics, viewsets
from .models import Book, PublicBook
from .serializers import BookSerializer, PublicBookSerializer
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


#Allows search function to search my books in the database
def search_books(request):
    query = request.GET.get('query', '')
    if query:
        books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
    else:
        books = Book.objects.all()
    
    results = [{'title': book.title, 'author': book.author, 'rating': book.rating} for book in books]
    return JsonResponse(results, safe=False)


# View to add books to the public library
def add_public_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        rating = request.POST.get('rating')
        PublicBook.objects.using('public_library').create(title=title, author=author, rating=rating)
        return JsonResponse({'message': 'Book added successfully'}, status=201)
    return render(request, 'add_public_book.html')


# View to list books in the public library
def ListPublicBooks(request):
    data = PublicBook.objects.using('public_library').all()
    context = {"public_books": data}
    return render(request, "public_library.html", context)


#Search books in the public library
def search_public_books(request):
    query = request.GET.get('query', '')
    if query:
        books = PublicBook.objects.using('public_library').filter(title__icontains=query) | PublicBook.objects.using('public_library').filter(author__icontains=query)
    else:
        books = PublicBook.objects.using('public_library').all()
    
    results = [{'title': book.title, 'author': book.author, 'rating': book.rating} for book in books]
    return JsonResponse(results, safe=False)


# Allows changing/deleting books in the public database -
class changePublicBook(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = PublicBook.objects.using('public_library').all()
    serializer_class = PublicBookSerializer
