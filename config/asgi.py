import os
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# 클라이언트의 요청은 channels가 먼저 받는다.
django_asgi_app = get_asgi_application()

# http 요청은 장고가 처리.
application = ProtocolTypeRouter({
    "http": django_asgi_app,
})

