from django.shortcuts import render
from rest_framework import generics
from .serializer import BookSerializer
from .models import Book
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# Create your views here.

class ListBookAPIView(generics.ListAPIView):
    queryset =  Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    
    
    def get_queryset(self):
        date = self.kwargs.get('date')
        queryset = super().get_queryset()  # Get the original queryset
        
        if date is not None and date != "null":
            queryset = queryset.filter(date=date)
        else:
            # Handle the case when date is "null" or None
            queryset = Book.objects.all()  
        return queryset
    
class CreateBookAPIView(generics.CreateAPIView):
    queryset =  Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)