from rest_framework import serializers

from users.models import CustomUser
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}, 
        }
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        
        instance = self.Meta.model(**validated_data)
        if instance is not None:
            instance.set_password(password)
        instance.save()
        
        return instance
    
class LoginSerialisers(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    
    class Meta:
        model=CustomUser
        fields = ['id', 'email', 'password', 'access', 'refresh']
        
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        request = self.context.get('request')
        
        user = authenticate(request, email=email, password=password)
        
        if not user:
            raise ValidationError('Incorrect email or password')
        
        user_token = user.get_token()
        
        return{
            'email' : user.email,
            'access' : str(user_token.get('access')),
            'refresh': str(user_token.get('refresh'))
        }
        
        