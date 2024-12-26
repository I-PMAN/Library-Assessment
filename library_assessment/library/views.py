from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.http import JsonResponse

import json

from library.models import Author, Book, Shelf

# @api_view(['GET'])
# @authentication_classes(JWTAuthentication)
# @permission_classes((IsAuthenticated,))
def get_and_create_books(request):
    try:
        if request.method == 'GET':
            all_books = Book.objects.all().values()
            return JsonResponse({
                "success" : True,
                "data" : list(all_books)
            })
       
        if request.method == 'POST':
            request_body = json.loads(request.body.decode('utf-8'))
            new_book = Book()
            for field, value in request_body.items():
                if hasattr(new_book, field):  # Check if the field exists in the model
                    setattr(new_book, field, value)
            new_book.save()
            return JsonResponse({
                "success" : True,
                "message" : "New Book created",
            })
            
    except Exception as error:
        return JsonResponse({
            "success" : False,
            "error" : str(error)
        })
    
def book_operations(request, id):
    #Get Book with sepcific id:
    try:            
        if request.method == 'GET':
            book = Book.objects.filter(id=str(id)).first()
            return JsonResponse({
                "success" : True,
                "data": book
            })

        if request.method == 'PUT':
            request_body = json.loads(request.body.decode('utf-8'))
            book = Book.objects.filter(id=str(id)).first()
            for field, value in request_body.items():
                if hasattr(book, field):  
                    setattr(book, field, value)
            book.save()
            
            return JsonResponse({
                "success" : True,
                "message" : "Book updated."
            })
            
        if request.method == 'DELETE':
            request_body = json.loads(request.body.decode('utf-8'))
            book = Book.objects.filter(id=str(id)).first()
            book.delete()
            
            return JsonResponse({
                "success" : True,
                "message" : "Book Deleted"
            })
            
    except Book.DoesNotExist:
        return JsonResponse({
            "success" : False,
            "error" : f"Book with id {str(id)} does not exist."
    })
    
    except Exception as error:
        return JsonResponse({
            "success" : False,
            "error" : str(error)
    })
            
def get_and_create_authors(request):
    try:
        if request.method == 'GET':
            all_authors = Author.objects.all().values()
            return JsonResponse({
                "success" : True,
                "data" : list(all_authors)
            })
        
        if request.method == 'POST':
            request_body = json.loads(request.body.decode('utf-8'))
            new_author = Author()
            for field, value in request_body.items():
                if hasattr(new_author, field):  # Check if the field exists in the model
                    setattr(new_author, field, value)
            new_author.save()
            return JsonResponse({
                "success" : True,
                "message" : "New author created."
            }) 
            
    except Exception as error:
        return JsonResponse({
            "success" : False,
            "error" : str(error)
        })

            
def author_operations(request, id):
    try:
        if request.method == 'GET':
            author_id = str(id)
            author = Author.objects.filter(id=author_id).first().values()
            return JsonResponse({
                "success" : True,
                "message" : str(author)
            })
            
        if request.method == 'PUT':
            request_body = json.loads(request.body.decode('utf-8'))
            author = Author.objects.filter(id=str(id)).first()
            for field, value in request_body.items():
                if hasattr(author, field):  
                    setattr(author, field, value)
            author.save()
            return JsonResponse({
                "success" : True,
                "message" : "Author updated."
            })
            
        if request.method == 'DELETE':
            request_body = json.loads(request.body.decode('utf-8'))
            author = Author.objects.filter(id=str(id)).first()
            author.delete()
            return JsonResponse({
                "success" : True,
                "message" : "Author deleted."
            })
            
    except Author.DoesNotExist:
        return JsonResponse({
            "success" : False,
            "error" : f"Author with id {id} does not exist."
        })
    except Exception as error:
        return JsonResponse({
            "success" : False,
            "error" : str(error)
        })

            

