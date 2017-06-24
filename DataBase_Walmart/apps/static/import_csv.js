$(document).ready(function () {
    $("#form_for_import").on("submit", function(e){
        e.preventDefault();
        var data = new FormData($('#form_for_import').get(0));
        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: data,
            cache: false,
            processData: false,
            contentType: false,
            dataType: 'json',
            success: function (data) {
                alert('Your add: '+data.count+ 'row(s)');
               console.log(data.count);
           },
           error: function (error) {
                console.log(error);
           }

        });
        var re_init = $('#mytable').DataTable();  // reload dataTable
        re_init.ajax.reload();

        $('#button_CSV').click(); // close modal window


    });


});