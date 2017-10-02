var serveid;


$(document).ready(function(){
//
//    function setID(){
//            var id = $(this).val();
//            console.log(id);
//    }
//
//    setID();

    var serveid2;


    $('.btn').click(function(){
       serveid = $(this).val();
       $('#btnmodalsave').val(serveid);
       console.log(serveid);
    });

    $('#btnmodalsave').click(function() {

        var minprice = document.getElementById("txtminprice").value;
        var maxprice = document.getElementById("txtmaxprice").value;
        serveid2 = $(this).val();


        console.log(serveid2);

        $.ajax({
                type:'POST',
                url:'/booknow/bidBook/',
                data:{
                    minprice:minprice,
                    maxprice:maxprice,
                    servid:serveid,
                    csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()

                },
                success:function(json){
                    console.log(json.replyBot)
                    if(json.replyBot === "success"){console.log("saved")}

                }
            });

    });

//    $(".btn").click(function(){
//            var id = $('.btn',this).html();
//            console.log(id);
//    })



//    $('.btn').click(function(e){
//        setID();
//    });
})


