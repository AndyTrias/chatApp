let socket = io();
socket.on('connect', function() {
        socket.emit("message", "hello");
    });

socket.addEventListener("message", function (msg){
    console.log(msg);

})