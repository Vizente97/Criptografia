$(document).ready(function () {
    
    $("#cifrado-btn").click(function(){
        $("#js-loader").css("display","block");
        $.ajax({
            url: '/cifrado',
            success: function(response){
                $("#features-container").css("display","block");
                console.log(response);
            },
            error: function(error){
            }
        });  
    });

});