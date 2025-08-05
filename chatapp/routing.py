from django.urls import re_path
from . import consumers


# "If the URL path starts with /ws/chat/, send the request to the ChatConsumer."
# routing.py sees the /ws/chat/ path and hands the request to your ChatConsumer class.

websocket_urlpatterns = [
    re_path(r'ws/socket-server/', consumers.ChatConsumer.as_asgi())
]






