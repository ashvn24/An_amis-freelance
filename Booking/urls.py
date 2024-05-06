from django.urls import path
from .views import ListBookAPIView, CreateBookAPIView

urlpatterns = [
    path('get/<str:date>', ListBookAPIView.as_view()),
    path('create/', CreateBookAPIView.as_view())
]
