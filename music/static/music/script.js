function AjaxCall (song) {
    console.log ("You clicked: " + song);
    var title = song[song.split('/').length-1];
    var splits = song.split('/');
    /* for (var i=0; i < splits.length; ++i) */
        /* console.log (splits[i]); */
    console.log (splits[splits.length-1]);

    /* console.log (song.split('/')); */
    document.getElementById ('title').innerHTML = splits[splits.length-1];
    $.ajax ({
        url: 'play',
        data: {
            'song': song,
        },
        type: 'post',
        success: function () { console.log ("Successfully send AJAX"); },
        error: function () { console.log ("Can't send AJAX request"); },
    });

}

$(document).ready (function () {
    $('.songs').click (function () {
        // console.log ("Clicked Div box");
        var song = this.a;
        $(song).click()
    });
});

$(document).ready (function () {
    $('#pause').click (function () {
        $.ajax ({
            url: 'pause',
            success: function () { console.log ("Song paused"); },
            error: function () { console.log ("Song can't be paused"); },
        });
    });
});

$(document).ready (function () {
    $('#resume').click (function () {
        $.ajax ({
            url: 'resume',
            success: function () { console.log ("Song resumed"); },
            error: function () { console.log ("Song can't be resumed"); },
        });
    });
});


$(document).ready (function () {

    // Server Side Events update
    var title = document.getElementById ('title');
    var eventSource = new EventSource ("stream");

    eventSource.onmessage = function (e) {
        title.innerHTML = e.data;
        console.log ("SSE Received: " + e.data);
    }
});
