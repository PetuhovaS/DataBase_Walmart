$(document).ready(function () {
    var form = $("#ExportToCSV");
    form.on("submit", function (e) {
        e.preventDefault();

        var data = {};
        data.id = 'ok-111';

        console.log(data);
        // Send data to back-end

        var url = form.attr("action");
        $.ajax({
            url: url,
            type: 'GET',
            data: data,
            cache: true,
            success: function () {
                console.log("OK_add");
                // alert(data.description);
            },
            error: function () {
                console.log("error_add");
                // alert(data.description);
            }
        });

    });

});