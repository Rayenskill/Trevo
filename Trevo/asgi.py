"""
ASGI config for Trevo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Trevo.settings')


# A Channels routing configuration is an ASGI application that is similar to
# a Django URLconf, in that it tells Channels what code to run when an
# HTTP request is received by the Channels server.

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
    }
)
