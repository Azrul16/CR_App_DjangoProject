# yourapp/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class StreamConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # Handle received data
        pass

    async def send_update(self, event):
        # Send data to the WebSocket
        await self.send(text_data=json.dumps(event))
