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

    $('#create-account').hide();

    $('#show-create-account').on({
        click: function(){
            $('#create-account').toggle();
        }
    });

});

$(document).ready(function() {

    $('#login').hide();

    $('#show-login').on({
        click: function(){
            $('#login').toggle();
        }
    });

});

$(document).ready(function() {
    $('#user-album-upload').submit(function(evt) {
        evt.preventDefault();

        const requestArgs = {
            'thumbnail': $('input[name="thumbnail"]').val()
        }

        const extensions = [".bmp", ".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png", ".tif", ".tiff", ".ico", ".cur"];

        const thumbnailURL = requestArgs['thumbnail'];

        $.ajax({
        type: "HEAD",
        url : requestArgs['thumbnail'],
        success: function(message,text,response){
            if (response.getResponseHeader('Content-Type').indexOf("image") === -1){

                for (const extension of extensions) {
                    if (thumbnailURL.indexOf(extension) !== -1) {
                        alert("Oops! Not a valid image! Please submit a valid link for your album thumbnail.");

                        return;
                    }
                }
                alert("Oops! Not a valid image! Please submit a valid link for your album thumbnail.");
            }
            else {
                evt.currentTarget.submit();
            }
        },
        error: function(request, status, error) {
            alert("Oops! Not a valid image! Please submit a valid link for your album thumbnail.")
        }
        }); 
    });
});

