import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model

from chatapp.models import Message # our Message Model.



# in a WebSocket connection, the 'scope' is like the 'request' object in http. Its a DICTIONNARY.
# self.scope['user'] : we can know who is the current Django User object because our webSocket is managed by AuthMiddlewareStack (asgi.py:26)
# self.scope['url_route'] : URL parameters aka path
# self.scope['url_route']['kwargs']['id'] allows to retrieve the other user's ID from the keywords in the URL.

# The routing.py file sees that both of these URLs match the same pattern 
# (ws/chat/<int:id>/). 
# It knows to send both connections to the same ChatConsumer.

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.current_user_id = self.scope['user'].id
        self.other_user_id = self.scope['url_route']['kwargs']['id']
        room_id_list = sorted([self.current_user_id, self.other_user_id])
        self.room_group_name = f"chat_{room_id_list[0]}_{room_id_list[1]}"

        # creates a Channel Layer (group) called room_group_name (ex. chat_1_2) + channel_name (generated) = chat_1_2-consumer1
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name # unique name of the instanciation of the ChatConsumer object.
        )
        self.accept()


    def disconnect(self):
        async_to_sync(self.channel_layer.group_discard)(self.room_group_name, self.channel_name)
    

    # server receives data - EXECUTED ONLY FOR THE PERSON WHO SENT THE MESSAGE.
    def receive(self, text_data): # text_data prints like '{"message":"gurtyo"}'
        text_data_json = json.loads(text_data) # so we convert the string into a Python dict {"message": "gurtyo"}
        message = text_data_json['message'] # and we get the value tied to the 'message' key. ("gurtyo")
        senderUsername = self.scope['user'].username

        # group_send sends the received message from one client to the other consumers (internally, not displayed) and our own so they can see it.
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message', # type = name of handler method !!
                'message':message,
                'senderUsername':senderUsername,
            }
        )

    # EXECUTED FOR EVERYBODY ONCE AN EVENT (MESSAGE) ARRIVES.
    # client -> server(receive) ->  server(group_send) -> channel_layer (everyone inside) -> calls the func 'type' for each consumer -> client on-screen
    def chat_message(self, event):
        message = event['message']
        senderUsername = event['senderUsername']

        self.send( # the message that gets displayed with chatSocket.onmessage
            text_data=json.dumps({
                'type':'chat_message',
                'message':message,
                'senderUsername':senderUsername
            })
        )
        
