let socket = io();
socket.on('connect', function() {
        socket.emit("evento", "hello");
    });

socket.addEventListener("mensaje", function (msg){
    alert(msg);

})