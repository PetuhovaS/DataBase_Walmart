$(document).ready(function () {
    $("#contact_form").on("submit", function(e) {
        var postData = $(this).serializeArray();
        var formURL = $(this).attr("action");
        $.ajax({
            url: formURL,
            type: "POST",
            data: postData,
            success: function(data) {
                console.log('ok')
            },
            error: function(jqXHR, status, error) {
                console.log(status + ": " + error);
            }
        });
        var re_init = $('#mytable').DataTable();  // reload dataTable
        re_init.ajax.reload();

        $('#button_close_upc').click(); // close modal window

        e.preventDefault();
    });

    $("#submitForm").on('click', function() {
        $("#contact_form").submit();
    });
});