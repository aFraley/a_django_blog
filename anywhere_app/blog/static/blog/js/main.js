/**
 * Created by alan on 2/6/17.
 */
$(function () {
    var comments = $('#comment-list');

    setInterval(function () {
        $.ajax({
            type: 'GET',
            url: 'http://localhost:8000/comments/' + topicId.toString() + '/',
            success: function (data) {
                comments.html(data);
            }
        });
    }, 120000);

});
