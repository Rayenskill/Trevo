"""
ASGI config for Trevo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chatapp.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Trevo.settings')


# A Channels routing configuration is an ASGI application that is similar to
# a Django URLconf, in that it tells Channels what code to run when an
# HTTP request is received by the Channels server.

# Looks at the type of protocol of an incoming request (http/ws) and sends it to the right handler.
# "http": get_asgi_application() = runs like normal, WSGI server.
# AuthMiddlewareStack takes the current user information and makes it available to your WebSocket consumer (know who sent what).
# URLRouter: WS Equivalent of urls.py for HTTP requests.
# URLRouter tells to go check chatapp.routing.websocket_urlpatterns to know what consumer gets the info.

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        'websocket': AuthMiddlewareStack(
            URLRouter(
                chatapp.routing.websocket_urlpatterns
            )
        )
    }
)
