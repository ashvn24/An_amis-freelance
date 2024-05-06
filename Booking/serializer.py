from .models import Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    customer_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Book
        fields = ['id', 'customer_name', 'time', 'date', 'user','Name','Phone']
        extra_kwargs ={
            "user": {"read_only": True}
        }
        
    def get_customer_name(self,obj):
        return obj.user.email