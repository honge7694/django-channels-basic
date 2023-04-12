import os
import app.routing
import chat.routing
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# 클라이언트의 요청은 channels가 먼저 받는다.
django_asgi_app = get_asgi_application()

# http 요청은 장고가 처리.
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    # 장고의 urls include와 유사한 역할 (urlpatterns를 최상위 라우터와 연결)
    # URLRouter는 path 리스트를 인자로 받는다.
    "websocket": AuthMiddlewareStack,
    
    # "websocket": URLRouter(
    #     app.routing.websocket_urlpatterns +
    #     chat.routing.websocket_urlpatterns
    # )
})

