from django.urls import re_path     # Esse re_path é para descrever expressões regulares
from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<nome_sala>\w+/$)', ChatConsumer)
]

