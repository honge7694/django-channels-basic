from django.urls import path
from app.consumers import EchoConsumer, LiveblogConsumer


# 장고의 urls urlpatterns와 유사한 역할 (URL 매핑)
# 장고 기본의 urls.py urlpatters와 다르게
# 장고에서 찾아서 읽어가는 것이 아니라, asgi.py 직접 임포트하여 지정하기때문에
# websocket_urlpatterns는 이름을 다르게하여도 괜찮다.
websocket_urlpatterns = [
    path("ws/liveblog/", LiveblogConsumer.as_asgi()),
    path("ws/echo/", EchoConsumer.as_asgi()),
]