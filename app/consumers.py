import json

from channels.generic.websocket import WebsocketConsumer, JsonWebsocketConsumer


class LiveblogConsumer(JsonWebsocketConsumer):
    groups = ["liveblog"] # 메세지를 받을 그룹명

    '''
    그룹을 통해 받은 메세지를 그대로 웹소켓 클라이언트에게 전달한다. (self.send(전달할_메세지))
    메세지의 type 값과 같은 이름의 메서드가 호출된다.

    ex) type "liveblog.post.created" => "liveblog_post_created" 메서드 호출 => 마침표(.)를 언더바(_)로 바꾼다.
    '''

    def liveblog_post_created(self, event_dict):
        # self.send(json.dumps(event_dict)) # WebsocketConsumer에서 사용.
        self.send_json(event_dict)

    def liveblog_post_updated(self, event_dict):
        # self.send(json.dumps(event_dict))
        self.send_json(event_dict)

    def liveblog_post_deleted(self, event_dict):
        # self.send(json.dumps(event_dict))
        self.send_json(event_dict)


class EchoConsumer(JsonWebsocketConsumer):
    '''
    웹소켓 클라이언트에서
    text frame 으로 보내면 text_data 인자에 값이 담겨지고
    binary data frame 으로 보내면 bytes_data 인자에 값이 담겨져 호출된다.
    '''
    def receive(self, content, **kwargs):
        # 새로운 text/bytes frame을 받을 때마다 호출된다.
        print("수신 : ", content)

        self.send_json({
            "content": content["content"],
            "user": content["user"],
        })

    # def receive(self, text_data=None, bytes_data=None):
    #     # 새로운 text/bytes frame을 받을 때마다 호출된다.
    #     obj = json.loads(text_data)
    #     print("수신 : ", obj)

    #     json_string = json.dumps({
    #         "content": obj['content'],
    #         "user": obj['user'],
    #     })

    #     self.send(json_string)