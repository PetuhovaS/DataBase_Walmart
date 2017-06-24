
$(document).ready(function () {
    $("#contact_form_del").on("submit", function (e) {
        var postData = $(this).serializeArray();
        var formURL = $(this).attr("action");
        $.ajax({
            url: formURL,
            type: "POST",
            data: postData,
            success: function (data, textStatus, jqXHR) {
                console.log('ok');

            },
            error: function(data) {
                console.log('error');
            }
        });
        var re_init = $('#mytable').DataTable();  // reload dataTable
        re_init.ajax.reload();

        $('#button_delete_close').click(); // close modal window

        e.preventDefault();
    });

    $("#submitForm_del").on('click', function() {
        $("#contact_form_del").submit();

    });
});
