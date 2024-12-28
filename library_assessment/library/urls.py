from django.urls import path, include
from library import views

urlpatterns = [
    path('books', views.get_and_create_books, name='get_and_create_books'),
    path('books/<int:id>', views.book_operations, name="book_operations"),
    path('authors', views.get_and_create_authors, name='get_all_authors'),
    path('authors/<int:id>', views.author_operations, name='author_operations'),
    path('suggested_books', views.get_suggested_books, name='get_suggested_books'),
    
]