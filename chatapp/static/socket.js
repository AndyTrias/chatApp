let socket = io();

socket.on('connect', function () {
    console.log('Connected to server');
});


document.addEventListener("DOMContentLoaded", function () {
    let input = document.querySelector("#message");

    document.querySelector("#sendmsg").addEventListener("click", function () {
        addMessage(input.value, "start");


        // Clear input and send message
        // Send contact to server to upload to database
        let data = {
            "message": input.value,
            "receiver": myContact
        };

        socket.emit("chatMessage", data);
        input.value = ""

    })

    socket.addEventListener("message", function (msg) {
        addMessage(msg, "end");
    });
});

// Abstraction to avoid coid repetition
function addMessage(msg, position) {
    let mainDiv = document.querySelector(".chat");

    // First Div
    let d = document.createElement("div");
    d.className = `d-flex flex-row justify-content-${position}`;

    // Paragraphs
    let p = document.createElement("p");
    p.innerHTML = msg;

    let p2 = document.createElement("p");
    p2.className = "small ms-3 mb-3 rounded-3 text-muted float-end";
    p2.innerHTML = new Date().toISOString();

    let d2 = document.createElement("div");

    if (position === "start") {
        // Image
        d.innerHTML += `<img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava5-bg.webp" alt="avatar 1" style="width: 45px; height: 100%;">`;
        p.className = "small p-2 ms-3 mb-1 rounded-3 message-content"
        d2.className = "message-container";
    }

    else {
        d2.className = "received";
        p.className = "small rounded-3 content"
    }

    // Append
    d2.appendChild(p);
    d2.appendChild(p2);
    d.appendChild(d2);
    if (position === "end")
        d.innerHTML += `<img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava6-bg.webp" alt="avatar 1" style="width: 45px; height: 100%;">`;

    mainDiv.appendChild(d)

}
