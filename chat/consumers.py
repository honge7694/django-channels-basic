from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer
from .models import Room


class ChatConsumer(JsonWebsocketConsumer):
    # SQUARE_GROUP_NAME = "square"
    # groups = [SQUARE_GROUP_NAME]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.group_name = ""


    def connect(self):
        user = self.scope["user"]

        if not user.is_authenticated:
            self.close()
        else:
            room_pk = self.scope["url_route"]["kwargs"]["room_pk"]
            self.group_name = Room.make_chat_group_name(room_pk=room_pk)

            async_to_sync(self.channel_layer.group_add)(
                # 첫번째 인자는 소속될 그룹명, 두번째 인자는 채널명
                self.group_name,
                self.channel_name,
            )

            self.accept()


    def disconnect(self, code):
        if self.group_name:
            async_to_sync(self.channel_layer.group_discard)(
                self.group_name,
                self.channel_name,
            )


    def receive_json(self, content, **kwargs):
        user = self.scope["user"]
        _type = content['type']

        if _type == "chat.message":
            sender = user.username
            message = content['message']
            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    "type": "chat.message",
                    "message": message,
                    "sender": sender,
                }
            )
        else:
            print(f"Invalid message type : ${_type}")


    def chat_message(self, message_dict):
        self.send_json({
            "type": "chat.message",
            "message": message_dict["message"],
            "sender": message_dict["sender"],
        })