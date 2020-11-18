"use strict";
// alert('This is my js code')


$(document).ready(function() {
    $('#user-album-form').click(function(evt) {
        console.log(evt);
        evt.preventDefault();

        $.ajax({

            url: "user-album-form",

            type: "GET",

            dataType: 'html',

            success: (res) => {
                $('#show-user-form').html(res);
            }
        });

    });
});

$(document).ready(function() {
    $('#user-album-upload').submit(function(evt) {
        evt.preventDefault();

        const requestArgs = {
            'thumbnail': $('select[name="thumbnail"]').val()
        }

        $.ajax({
        type: "HEAD",
        url : requestArgs['thumbnail'],
        success: function(message,text,response){
            console.log(response);
            console.log(response.getResponseHeader('Content-Type'));
            if(response.getResponseHeader('Content-Type').indexOf("image") === -1){
            alert("Not an image");
        }
        } 
    });
    });
});

