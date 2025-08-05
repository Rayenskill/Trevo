import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        # in the connect() method, the send method sends from the server to the client a message
        # to confirm that the WebSocket connection was established successfully.
        # the text has to be in json form since in index.html, the JS script awaits a JSON :
        # chatSocket.onmessage = function(e){
        #      let data = JSON.parse(e.data)
        #        console.log('Data: ', data)
        #   }

        self.send(text_data=json.dumps({
            'type':'connection_established',
            'message':'You are now connected.'
        }))

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print('Message: ', message)
        

