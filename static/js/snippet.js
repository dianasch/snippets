"use strict";
// alert('This is my js code')



$(document).ready(function() {

    $('#user-album-form').on({
        click: function(){
            if ($('#show-user-form').is(":visible")) {
                $('#show-user-form').hide();
            }
            else {
                $('#show-user-form').show();
            }
        }
    });

});

$(document).ready(function() {

    $('#create-account').hide();

    $('#show-create-account').on({
        click: function(){
            $('#create-account').toggle();
            if (($('#show-login').is(":visible")) && ($('#test-it-out').is(":visible"))) {
                $('#show-login').hide();
                $('#test-it-out').hide();
            }
            else {
                $('#show-login').show();
                $('#test-it-out').show();
            }
        }
    });

});

$(document).ready(function() {

    $('#login').hide();

    $('#show-login').on({
        click: function(){
            $('#login').toggle();
            if (($('#show-create-account').is(":visible")) && ($('#test-it-out').is(":visible"))) {
                $('#show-create-account').hide();
                $('#test-it-out').hide();
            }
            else {
                $('#show-create-account').show();
                $('#test-it-out').show();
            }
        }
    });

});

$(document).ready(function() {
    $('#user-album-upload').submit(function(evt) {
        evt.preventDefault();

        const requestArgs = {
            'thumbnail': $('input[name="thumbnail"]').val()
        }

        // Array of possible image extensions
        const extensions = [".bmp", ".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png", ".tif", ".tiff", ".ico", ".cur"];

        const thumbnailURL = requestArgs['thumbnail'];

        $.ajax({
        type: "HEAD",
        url : requestArgs['thumbnail'],
        success: function(message,text,response){
            // Check if MIME content from header contains string `image`
            // If indexOf returns -1, URL is not an image path
            if (response.getResponseHeader('Content-Type').indexOf("image") === -1){

                // Safeguard measure if MIME content isn't correct
                // Check if any of the image extensions appear in thumbnail URL
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

