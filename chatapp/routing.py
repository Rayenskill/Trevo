from django.urls import re_path
from . import consumers


# "If the URL path starts with /ws/socket-server/, send the request to the ChatConsumer."
# routing.py sees the /ws/socket-server/ path and hands the request to your ChatConsumer class.

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi())
]

# (?P<room_name>\w+) Captures a "room\_name" parameter consisting of one or more words (w+)
# /$ Matches the literal forward slash and indicates the end of the URL pattern.





