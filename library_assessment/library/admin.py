from django.contrib import admin

# Register your models here.

from library.models import Author, Book, Shelf

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Shelf)
