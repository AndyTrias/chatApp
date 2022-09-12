let socket = io();



document.addEventListener("DOMContentLoaded", function (){
    let input = document.querySelector("#message");
    document.querySelector("#sendmsg").addEventListener("click", function(){
        socket.emit("chatMessage", input.value);
        input.value = ""
    })

    socket.addEventListener("message", function (msg) {
        console.log(msg);
        // let p = document.createElement("p");
        // p.className = "small p-2 ms-3 mb-1 rounded-3";
        // p.innerHTML = msg;
        // document.querySelector("#chats").appendChild(p);

    });

})




/* $(document).ready(function(){
    $('.contact').on('click',function(){
     var layout = $(this).data('contacto');
     console.log(layout);
      $.ajax({
       url: "/chat",
       type: "get",
       data: {layout: layout},
       success: function(response) {
         var new_html = response.html;
       },
      });     
   });
 }); */