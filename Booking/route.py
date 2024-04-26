from django.urls import path
from .consumers import AdminConsumer

websocket_urlpatterns = [
    path('ws/book/',  AdminConsumer.as_asgi()), 
]