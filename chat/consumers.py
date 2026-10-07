import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.roomGroupName = "group_chat_gfg"
        await self.channel_layer.group_add(
            self.roomGroupName, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.roomGroupName,
            {
                "type": "sendMessage",
                "message": data["message"],
                "username": data["username"],
            },
        )

    async def sendMessage(self, event):
        await self.send(text_data=json.dumps({
            "message": event["message"],
            "username": event["username"],
        }
        )
        )
