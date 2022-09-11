let socket = io();
socket.on('connect', function() {
        socket.emit("evento", "hello");
    });

socket.addEventListener("mensaje", function (msg){
    //alert(msg);

})

document.addEventListener("DOMContentLoaded", function (){

    document.querySelector(".enviar").addEventListener("click", function(){
        let message = document.querySelector("#mensaje").value;
        socket.emit("mensaje", message);
    })

})