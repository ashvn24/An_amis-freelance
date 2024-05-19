from django.urls import  path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('token/refresh',TokenRefreshView.as_view(),name= 'token_refresh'),
    path('reg/', UserRegAPIView.as_view()),
    path('log/', LoginAPIView.as_view()),
    path('list/', ManageUsersAPIView.as_view()),
    path('update/<int:id>', ManageUserAPIView.as_view()),
]
