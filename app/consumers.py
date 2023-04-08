import json

from channels.generic.websocket import WebsocketConsumer


class EchoConsumer(WebsocketConsumer):
    # 웹소켓 클라이언트에서
    # text frame 으로 보내면 text_data 인자에 값이 담겨지고
    # binary data frame 으로 보내면 bytes_data 인자에 값이 담겨져 호출된다.

    def receive(self, text_data=None, bytes_data=None):
        # 새로운 text/bytes frame을 받을 때마다 호출된다.
        obj = json.loads(text_data)
        print("수신 : ", obj)

        json_string = json.dumps({
            "content": obj['content'],
            "user": obj['user'],
        })

        self.send(json_string)