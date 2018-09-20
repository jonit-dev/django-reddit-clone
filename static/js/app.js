$(function () {

    config = {
        "hostUrl": "http://localhost:8000/"
    };

    function vote(downvote_upvote, postId, csrf_token) {
        // make ajax call
        $.ajax({
            type: 'POST',
            url: `${config.hostUrl}posts/${postId}/${downvote_upvote}`,
            dataType: 'json',
            data: {
                'csrfmiddlewaretoken': csrf_token,
                value: 1
            },
            success: function (data, status) {
                if (data.response == "success") {

                    let decorator = `<div class="alert alert-${data.alert.type}" role="alert">
  ${data.alert.message}
</div>`;

                    //show success message
                    $(".alert-list").append(decorator);

                    //update voting
                    console.log($(`[data-post-id=${postId}]`).children(".votes-total").html(data.votes));

                    setTimeout(() => {

                        $(".alert-list").html("");

                    },3000)

                }

            },
            error: function (req, errorType, errorMsg) {
                console.log('Ajax Call Error type:' + errorType + ' - ' + errorMsg)
            }
        });
    }

    $(".downvote").on("click", function () {

        let postId = $(this).parent().attr("data-post-id");
        let csrf_token = $(this).parent().attr("data-post-csrf");

        console.log("Downvoting -> " + postId);

        vote("downvote", postId, csrf_token);

    });


    $(".upvote").on("click", function () {

        let postId = $(this).parent().attr("data-post-id");
        let csrf_token = $(this).parent().attr("data-post-csrf");

        console.log("upvoting -> " + postId);

        vote("upvote", postId, csrf_token);

    });


});