// https://www.youtube.com/watch?v=cw8-KFVXpTE
// ws: instead of http: for a WebSocket a persistent two-way connection
// window.location.host is a JS variable that contains the current root URL ex. example.com or 127.0.0.1:8000
// ws/chat/${otherUserId} This is the specific path on the server where the Django WebSocket "consumer" is listening.
const connectButton = document.getElementById("connect-button")
const otherUserIdInput = document.getElementById("other-user-id")
connectButton.addEventListener('click', function(){
    otherUserId = otherUserIdInput.value.trim()
    let url = `ws://${window.location.host}/ws/chat/${otherUserId}/`; // creates a specific URL for a WS connection chat.
    const chatSocket = new WebSocket(url);
    console.log("WebSocket estalibshed!")

    // PART 1 : RECEIVING AND DISPLAYING A MESSAGE ON THE CLIENT.
    // When a message arrives on this specific chatSocket connection, run this function.
    // JSON.parse converts the event object into a JSON object which can then be manipulated in JS more freely.
    chatSocket.onmessage = function(event){
        let data = JSON.parse(event.data)
        console.log('Data: ', data) // the data here is the message we sent in the connect() method in consumers.py\

        if(data.type === 'chat_message'){           // type is defined in consumer.py
            let messages = document.getElementById('messages')
            messages.insertAdjacentHTML('beforeend', `<div> // basically inserts the message text inside the 'messages' div.
                <p>${data.senderUsername}: ${data.message}</p>
                </div>`)
        }
    }

    // PART 2 : SENDING A MESSAGE (which triggers the part 1 function to display it).

    const senderUsername = document.getElementById('username').innerText
    let form = document.getElementById('form') // document.getElementById references <form id='form'>
    // addEventListener tells the client to wait for an event of type 'submit' (when submitting the form)
    // event.target (<form>) .message (form name='message') .value (the text written) into a variable message.
    // Basically, Client types a message ----> received by the server with the consumer receive()

    form.addEventListener('submit', function(event){ 
        event.preventDefault()              // prevents the default behavior of a form, aka reloading the page
        let message = event.target.message.value
        chatSocket.send(JSON.stringify({    // When sending data to a web server, the data has to be a JSON string.
            'message': message,
            'senderUsername':senderUsername
        }))
        form.reset()
    })
})




            