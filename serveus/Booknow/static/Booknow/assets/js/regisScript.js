$(document).ready(function(){
   $("#txtPass").keypress(function(e){
        if(e.keyCode ==13){
            var name = document.getElementById("txtName").value;
            var email = document.getElementById("txtEmail").value;
            var pass = document.getElementById("txtPass").value;

            console.log(email+ "==" + pass);

            $.ajax({
                type:'POST',
                url:'/booknow/regis/',
                data:{
                    usrName:name,
                    usrEmail:email,
                    usrPass:pass,
                    csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()

                },
                success:function(json){
                    console.log(json.replyBot)
                    if(json.replyBot === "success"){location.href ="/jobnapper"}

                }
            });
        }
    })

})