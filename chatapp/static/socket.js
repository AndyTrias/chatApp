let socket = io();

socket.on('connect', function() {
    console.log('Connected to server');
});


document.addEventListener("DOMContentLoaded", function (){
    let input = document.querySelector("#message");

    document.querySelector("#sendmsg").addEventListener("click", function(){
        addMessage(input.value, "start");


       // Clear input and send message
        let data  = { "message": input.value,
                  "receiver": myContact};

        socket.emit("chatMessage", data);
        input.value = ""

    })

    socket.addEventListener("message", function (msg) {
        addMessage(msg, "end");
    });
});

 function addMessage(msg, position) {
        let mainDiv = document.querySelector("#chats");

        // First Div
        let d = document.createElement("div");
        d.className = `d-flex flex-row justify-content-${position}`;

        // Paragraph
        let p = document.createElement("p");
        p.innerHTML = msg;
        p.className = "small p-2 ms-3 mb-1 rounded-3"
        p.style.backgroundColor = "#f5f6f7"

        // Append
        d.appendChild(p);
        mainDiv.appendChild(d);
    }
