from django.shortcuts import render
from .models import CustomUser
from rest_framework import generics, status
from .serializer import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


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
    
class ManageUsersAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ListUserSerializer
    
    
class ManageUserAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    parser_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ListUserSerializer
    lookup_field = 'id'
    
    def perform_update(self, serializer):
        instance = serializer.instance
        instance.is_active = not instance.is_active
        serializer.save()