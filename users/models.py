from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from users.manager import UserManager
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.
class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects=UserManager()
    
    def __str__(self):
        return self.email
    
    def get_token(self):
        refresh = RefreshToken.for_user(self)
        
        return{
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }
        
    
    
