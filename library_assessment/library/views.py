from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.http import JsonResponse

# @api_view(['GET'])
# @authentication_classes(JWTAuthentication)
# @permission_classes((IsAuthenticated,))
def get_all_books(request):
    if request.method == 'GET':
        try:
            return JsonResponse({
                "success" : True,
                "message" : "get all books"
            })
        except Exception as error:
            return JsonResponse({
                "success" : False,
                "error" : str(error)
            })
    if request.method == 'POST':
        try:
            return JsonResponse({
                "success" : True,
                "message" : "Created new book"
            })
        except Exception as error:
            return JsonResponse({
                "success" : False,
                "error" : str(error)
            })
    
def book_operations(request, id):
    if request.method == 'GET':
        try:
            return JsonResponse({"message": "Get one book"})

        except Exception as error:
            return JsonResponse({
                "success" : False,
                "error" : str(error)
            })

    if request.method == 'PUT':
        try:
            return JsonResponse({
                "success" : True,
                "message" : "Editing book"
            })
        except Exception as error:
            return JsonResponse({
                "success" : False,
                "error" : str(error)
            })
            
    if request.method == 'DELETE':
        try:
            return JsonResponse({
                "success" : True,
                "message" : "Deleting book"
            })
        except Exception as error:
            return JsonResponse({
                "success" : False,
                "error" : str(error)
            })
            
def get_authors(request):
    if request.method == 'GET':
        try:
            return JsonResponse({
                "message" : "All Authors"
            })
        except Exception as error:
            return JsonResponse({
                "error" : str(error)
            })
    
    if request.method == 'POST':
        try:
            return JsonResponse({
                "message" : "Creating a new author"
            })
        except Exception as error:
            return JsonResponse({
                "error" : str(error)
            })
            
def author_operations(request, id):
    if request.method == 'GET':
        try:
            return JsonResponse({
                "message" : "Get author by id"
            })
        except Exception as error:
            return JsonResponse({
                "error" : str(error)
            })
    if request.method == 'PUT':
        try:
            return JsonResponse({
                "message" : "Updating Author"
            })
        except Exception as error:
            return JsonResponse({
                "error" : str(error)
            })
            
    if request.method == 'DELETE':
        try:
            return JsonResponse({
                "message" : "Deleting Author"
            })
        except Exception as error:
            return JsonResponse({
                "error" : str(error)
            })