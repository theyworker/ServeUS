$(document).ready(function(){
   $("#txtPass").keypress(function(e){
        if(e.keyCode ==13){
            var address = document.getElementById("txtAddress").value;
            var phoneNo = document.getElementById("phNo").value;
            var name = document.getElementById("txtName").value;
            var email = document.getElementById("txtEmail").value;
            var pass = document.getElementById("txtPass").value;
            var conpass = document.getElementById("txtConfirm").value;

            console.log(email+ "==" + pass);

            $.ajax({
                type:'POST',
                url:'/booknow/regis/',
                data:{
                    usrName:name,
                    usrEmail:email,
                    usrPass:pass,
                    usrAddress:address,
                    usrPh:phoneNo,
                    usrConPass:conpass,
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