"""
ASGI config for simple_chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import simple_chat.urls
import chat.urls

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_chat.settings')

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            #simple_chat.urls.websocket_urlpatterns,
            chat.urls.websocket_urlpatterns,
        )
    ),
	})
