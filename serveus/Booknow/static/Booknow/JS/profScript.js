$(document).ready(function(){
    $('#btnSub').click(function() {
        var serviceType = $('#cmbSer option:selected').val();
        var location = document.getElementById("txtLocation").value;
        var description = document.getElementById("txtDescription").value;
        var d = document.getElementById("txtDate").value;
        var date = new Date(d);
        var properdate = date.getFullYear()+"-"+date.getMonth()+"-"+date.getDate();
        console.log(serviceType);

        $.ajax({
                type:'POST',
                url:'/booknow/regBook/',
                data:{
                    serviceType:serviceType,
                    description:description,
                    location:location,
                    date:properdate,
                    csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()

                },
                success:function(json){
                    console.log(json.replyBot)
                    if(json.replyBot === "success"){console.log("saved")}

                }
            });

    });
     $('#btnApply').click(function() {
            serveid = $(this).val();

            $.ajax({
                type:'POST',
                url:'/booknow/applyBooking/',
                data:{
                    serveid:serveid,
                    csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()

                },
                success:function(json){
                    console.log(json.replyBot)
                    if(json.replyBot === "success"){console.log("saved")}

                }
            });

     });
})