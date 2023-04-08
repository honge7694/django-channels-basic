import asyncio
import os
import django
from channels.layers import get_channel_layer


os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings"
django.setup()

async def main():
    # 채널 레이어는 웹소켓과 다르게 내부적으로 직렬화를 수행.
    channel_layer = get_channel_layer() 
    message_dict = {'content': 'world'}

    # 'hello' 채널에 메세지를 보낸다.
    await channel_layer.send('hello', message_dict) 

    # 'hello' 채널로부터 메세지를 읽는다.
    response_dict = await channel_layer.receive('hello')
    is_equal = message_dict == response_dict
    print("송신/수신 데이터가 같습니까?", is_equal)

asyncio.run(main())
