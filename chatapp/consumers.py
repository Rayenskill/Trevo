import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.send(text_data=json.dump({
            'type':'connection_established',
            'message':'You are now connected!'
        }))

