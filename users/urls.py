from django.urls import  path
from .views import *

urlpatterns = [
    path('reg/', UserRegAPIView.as_view()),
    path('log/', LoginAPIView.as_view()),
    path('list/', ManageUsersAPIView.as_view()),
    path('update/<int:id>', ManageUserAPIView.as_view()),
]
