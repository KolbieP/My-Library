from django.urls import path
from . import views

urlpatterns = [
    path('books', views.showBooks.as_view({'get':'list'})),
    path('books/<int:pk>', views.changeBook.as_view()),
    path('add', views.newBook.as_view()),
]