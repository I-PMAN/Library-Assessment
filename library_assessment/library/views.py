from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import  BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
import json

from library.models import Author, Book, Shelf

# @api_view(['GET'])
# @authentication_classes(JWTAuthentication)
# @permission_classes((IsAuthenticated,))
def get_and_create_books(request):
    try:
        if request.method == 'GET':
            request_body = json.loads(request.body.decode('utf-8'))
            search = request.GET.get('search')
            if 'author' in search:
                query = search.split("=")
                books = Book.objects.filter(author=query[1])
                return JsonResponse({
                    "success" : True,
                    "data" : list(books.values())
                })
            elif 'title' in search:
                query = search.split("=")
                books = Book.objects.filter(title=query[1])
                return JsonResponse({
                    "success" : True,
                    "data" : list(books.values())
                })
                
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

@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['POST'])            
def register(request):
    try:
        """
        API endpoint for user registration
        """
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        if not username or not email or not password:
            return JsonResponse({
                "success" : False,
                "error": "All fields are required"
            })

        if User.objects.filter(username=username).exists():
            return JsonResponse({
                "success" : False,
                "error": "Username already exists"
            })

        user = User.objects.create_user(username=username, email=email, password=password)
        tokens = get_tokens_for_user(user)
        return Response({
            "success": True,
            "access": tokens['access'],
            "refresh": tokens['refresh']
        })

    except Exception as error:
        return JsonResponse({
            "success" : False,
            "error" : str(error)
        })
@csrf_exempt
@api_view(['POST']) 
def login(request):
    try:
        """
        API endpoint for user login
        """
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({
                "success" : False,
                "error": "Both username and password are required"
            })
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({
                "success" : False,
                "error": "Invalid credentials"
            })

        tokens = get_tokens_for_user(user)

        return Response({
            "success": "True",
            "message": "Login successful",
            "tokens": tokens
            })
    
    except Exception as error:
        return JsonResponse({
            "success" : False,
            "error" : str(error)
        })



def get_tokens_for_user(user):
    """
    Generate JWT tokens for a user.
    """
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def get_suggested_books(request):
    try:
        pass
    except Exception as error:
        return JsonResponse({
            "success" : False,
            "error" : str(error)
        })