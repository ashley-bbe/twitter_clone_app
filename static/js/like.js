$(function () {
    // Global valuable
    var is_liked = false;

    // Clicked like icon
    $('.js-like').click(function () {
        var id = $(this).data('id');
        var like_count_obj = $(this).parent().find('.js-like-count');
        var like_count = Number(like_count_obj.html());
        var sakura_icon_obj = $(this).find('img');
        var sakura_icon_url = sakura_icon_obj.attr('src');

        if (sakura_icon_url == JS_ICON_SAKURA_BLACK) {
            // It has not been liked
            // Increase the count of likes
            $.ajax({
                url: '/tweetLikeAdd/' + id + '/',
                type: 'POST',
                data: {},
                headers: { 'X-CSRFToken': JS_CSRFTOKEN }
            })
                // Successful
                .done((data) => {
                    // Increase
                    var new_like_count = like_count + 1;
                    like_count_obj.html(new_like_count);

                    // Change the icon 
                    sakura_icon_obj.attr('src', JS_ICON_SAKURA_PINK);
                })

                // Failure
                .fail((data) => {
                    alert('Error');
                    console.log(data);
                });
        } else {

            // It has been liked
            // Decrease the count of likes
            $.ajax({
                url: '/tweetLikeSubtract/' + id + '/',
                type: 'POST',
                data: {},
                headers: { 'X-CSRFToken': JS_CSRFTOKEN }
            })
                // Successful
                .done((data) => {
                    // Decrease
                    var new_like_count = like_count - 1;
                    like_count_obj.html(new_like_count);

                    // Change the button to pink
                    sakura_icon_obj.attr('src', JS_ICON_SAKURA_PINK);
                })
                // Failure
                .fail((data) => {
                    alert('Error');
                    console.log(data);
                });
        }
    });

});

