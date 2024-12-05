import json
from channels.generic.websocket import AsyncWebsocketConsumer

class AudioConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'audio_room'
        self.room_group_name = f'audio_{self.room_name}'
        
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    # Receive audio data from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        audio_data = text_data_json['audio']
        
        # Send audio data to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'audio_message',
                'audio': audio_data
            }
        )

    # Receive audio data from room group
    async def audio_message(self, event):
        audio_data = event['audio']
        
        # Send audio data to WebSocket
        await self.send(text_data=json.dumps({
            'audio': audio_data
        }))
