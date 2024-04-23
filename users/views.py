from django.shortcuts import render
from .models import CustomUser
from rest_framework import generics, status
from .serializer import *
from rest_framework.response import Response


class UserRegAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        
        return Response(response.data, status=status.HTTP_201_CREATED)
    
    
class LoginAPIView(generics.CreateAPIView):
    serializer_class = LoginSerialisers
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data= request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status= status.HTTP_200_OK)