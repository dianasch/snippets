"use strict";
// alert('This is my js code')

const currentPage = window.location.href
const album_id = currentPage[(currentPage.length) - 1]

$(window).on('load', () => {
    $('#create-snippet').on('submit', (evt) => {
        evt.preventDefault();

        $.ajax({

            url: `/albums/${album_id}/snippet`,

            type: "GET",

            dataType: 'text',

            success: (res) => {
                console.log('loaded', res);
                $('#display-snippet').html(res);
            }
        });

    });
});

// $.get('/albums/1/snippet', (res) => {
//     $('#display-snippet').html(res);
// });


// $('#create-snippet').on('click', (evt) => {
//     evt.preventDefault();

//     const snippet = sessionStorage.getItem('snippet');

//     ('#display-snippet').html(snippet);
// });

// $('#save-snippet').on('submit', (evt) => {
//     evt.preventDefault();

//     const snippet = $.get('/albums/<album_id>/snippet', (res) => {
        
//     })
//     $.post('/albums/<album_id>/snippet/save', snippet, (res) => {
        
//     })
// });