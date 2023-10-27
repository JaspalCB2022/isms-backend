from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from .models import User
from . import serializers
from django.contrib.auth.hashers import check_password, make_password
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)

from rest_framework_simplejwt.tokens import RefreshToken


class UserLogin(CreateAPIView):
    serializer_class = serializers.UserLoginSerializer    
    def post(self, request,  *args, **kwargs):
        serializer = self.get_serializer(data=request.POST)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        print("user user >>>", user)
        serializer = serializers.UserSerializer(user)
        print("user user  serializer>>>", serializer)


        token = RefreshToken.for_user(user)
        
        data = serializer.data
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return Response(data, status=status.HTTP_200_OK)
        # email = request.POST.get('email')
        # password = request.POST.get('password')

        # tempuserObj = Users.objects.get(email=email)
        # user = check_password(password ,tempuserObj.password)

        # if user is not None:
        #     # Authentication successful
        #     #token, created = Token.objects.get_or_create(user=user)
        #     refresh = RefreshToken.for_user(user=tempuserObj)
        #     print("refresh >>>", refresh)
        #     return Response({'token': refresh})
        #     #return Response({'message': 'Login successful', 'data': token}, status=status.HTTP_200_OK)
        # else:
        #     # Invalid credentials
        #     return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



# class UserLoginView(
 # APIView, # Basic View class provided by the Django Rest Framework
#  UpdateModelMixin, # Mixin that allows the basic APIView to handle PUT HTTP requests
#  DestroyModelMixin, # Mixin that allows the basic APIView to handle DELETE HTTP requests
#):

  # def get(self, request, id=None):
  #   if id:
  #     print("request >>>", request.GET)
  #     # If an id is provided in the GET request, retrieve the Todo item by that id
  #     try:
  #       # Check if the todo item the user wants to update exists
  #       queryset = Users.objects.get(id=id)
  #     except Users.DoesNotExist:
  #       # If the todo item does not exist, return an error response
  #       return Response({'errors': 'This user does not exist.'}, status=400)
    
      
  #     # Serialize todo item from Django queryset object to JSON formatted data
  #     read_serializer =UserSerializer(queryset).data
    
  #   else:
  #     # Get all todo items from the database using Django's model ORM
  #     queryset = Users.objects.all()

  #     # Serialize list of todos item from Django queryset object to JSON formatted data
  #     read_serializer = UserSerializer(queryset, many=True).data

  #   #Return a HTTP response object with the list of todo items as JSON
  #   return Response(read_serializer, status=200)
   


  # def post(self, request):
    #print("request.data <>>>", request.data)
    
    # Pass JSON data from user POST request to serializer for validation
    # create_serializer = TodoSerializer(data=request.data)

    # # Check if user POST data passes validation checks from serializer
    # if create_serializer.is_valid():

    #   # If user data is valid, create a new todo item record in the database
    #   todo_item_object = create_serializer.save()

    #   # Serialize the new todo item from a Python object to JSON format
    #   read_serializer = TodoSerializer(todo_item_object)

    #   # Return a HTTP response with the newly created todo item data
    #   return Response(read_serializer.data, status=201)

    # # If the users POST data is not valid, return a 400 response with an error message
    # return Response(create_serializer.errors, status=400)


#   def put(self, request, id=None):
#     try:
#       # Check if the todo item the user wants to update exists
#       todo_item = Todo.objects.get(id=id)
#     except Todo.DoesNotExist:
#       # If the todo item does not exist, return an error response
#       return Response({'errors': 'This todo item does not exist.'}, status=400)

#     # If the todo item does exists, use the serializer to validate the updated data
#     update_serializer = TodoSerializer(todo_item, data=request.data)

#     # If the data to update the todo item is valid, proceed to saving data to the database
#     if update_serializer.is_valid():

#       # Data was valid, update the todo item in the database
#       todo_item_object = update_serializer.save()

#       # Serialize the todo item from Python object to JSON format
#       read_serializer = TodoSerializer(todo_item_object)

#       # Return a HTTP response with the newly updated todo item
#       return Response(read_serializer.data, status=200)

#     # If the update data is not valid, return an error response
#     return Response(update_serializer.errors, status=400)


# #   def delete(self, request, id=None):
#     try:
#       # Check if the todo item the user wants to update exists
#       todo_item = Todo.objects.get(id=id)
#     except Todo.DoesNotExist:
#       # If the todo item does not exist, return an error response
#       return Response({'errors': 'This todo item does not exist.'}, status=400)

#     # Delete the chosen todo item from the database
#     todo_item.delete()

#     # Return a HTTP response notifying that the todo item was successfully deleted
#     return Response(status=204)