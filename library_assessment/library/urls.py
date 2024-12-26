from django.urls import path, include
from library import views

urlpatterns = [
    path('books', views.get_all_books, name='get_all_books'),
    path('books/<int:id>', views.book_operations, name="book_operations"),
    path('authors', views.get_authors, name='get_all_authors'),
    path('authors/<int:id>', views.author_operations, name='author_operations'),
    
]