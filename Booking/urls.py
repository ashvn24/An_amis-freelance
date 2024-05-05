from django.urls import path
from .views import ListBookAPIView

urlpatterns = [
    path('get/<str:date>', ListBookAPIView.as_view())
]
