from django.urls import path
from . import views

urlpatterns = [
    path('books', views.showBooks.as_view({'get':'list'})),
    path('books/<int:pk>', views.changeBook.as_view()),
    path('add', views.newBook.as_view()),
    path('', views.index, name='index'),
    path('library', views.ListshowBooks, name='book'),
    path('search/', views.search_books, name='search_books'),
    path('all_books/', views.all_books, name='all_books'),
    path('public_all_books/', views.all_public_books, name='all_public_books'),
    path('public_library/add', views.add_public_book, name='add_public_book'),
    path('public_library', views.ListPublicBooks, name='public_library'),
    path('public_library/search/', views.search_public_books, name='search_public_books'),
    path('public_library/<int:pk>', views.changePublicBook.as_view(), name='change_public_book'),
]