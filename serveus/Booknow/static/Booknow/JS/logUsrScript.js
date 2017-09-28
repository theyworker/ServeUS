$(document).ready(function(){
   $("#txtPass").keypress(function(e){
        if(e.keyCode ==13){
            var email = document.getElementById("txtEmail").value;
            var pass = document.getElementById("txtPass").value;

            console.log(email+ "==" + pass);

            $.ajax({
                type:'POST',
                url:'/booknow/verLoginUser/',
                data:{
                    usrEmail:email,
                    usrPass:pass,
                    csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()

                },
                success:function(json){
                    console.log("successfulllllllllll")
                    if(json.replyBot === "success"){location.href ="/booknow/profile/"}

                }
            });
        }
    })

})


function validate(){
        var email = document.getElementById("txtEmail").value;
        var pass = document.getElementById("txtPass").value;

        console.log(email+ "==" + pass);

        $.ajax({
            type:'POST',
            url:'/booknow/verLoginUser/',
            data:{
                usrEmail:email,
                usrPass:pass,
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()

            },
            success:function(json){
                console.log("successfulllllllllll")
                if(json.replyBot === "success"){location.href ="/booknow/profile/"}

            }
        });
}