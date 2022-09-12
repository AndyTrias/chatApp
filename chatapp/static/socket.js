let socket = io();

socket.on('connect', function() {
    console.log('Connected to server');
});


document.addEventListener("DOMContentLoaded", function (){
    let input = document.querySelector("#message");

    document.querySelector("#sendmsg").addEventListener("click", function(){
        socket.emit("chatMessage", input.value);
        input.value = ""
    })

    // socket.addEventListener("message", function (msg) {
    //     console.log(msg);
    //     // let mainDiv = document.querySelector("#chats");
    //     // let d = document.createElement("div");
    //     // let p = document.createElement("p");
    //     // p.innerHTML = msg;
    //     // p.className = "small p-2 ms-3 mb-1 rounded-3"
    //     // p.style.backgroundColor = "#f5f6f7"
    //     // d.appendChild(p);
    //     // mainDiv.appendChild(d);
    //
    //
    //     // Ad alternative to the above code is to use the following code:
    //
    //     // <div className="d-flex flex-row justify-content-start">
    //     //     <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava6-bg.webp"
    //     //          alt="avatar 1" style="width: 45px; height: 100%;">
    //     //         <div>
    //     //             <p className="small p-2 ms-3 mb-1 rounded-3" style="background-color: #f5f6f7;">how are you?</p>
    //     //             {#                            <p class="small p-2 ms-3 mb-1 rounded-3" style="background-color: #f5f6f7;">{{message.content}}</p>#}
    //     //             {#                            <p class="small ms-3 mb-3 rounded-3 text-muted float-end">{{message.sentAt}}</p>#}
    //     //         </div>
    //     // </div>
    //
    // });

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