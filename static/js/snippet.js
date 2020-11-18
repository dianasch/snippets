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
