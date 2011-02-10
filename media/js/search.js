function handle_keyup() {
    var search_text = $('#search').val();
    jQuery.ajax({url: '/search?search=' + search_text, 
                 success: function (data,status,xhr) {
                     $('#service-list').replaceWith(data);
                 }
                });
}


google.setOnLoadCallback(
    function() {
        $('#search').bind('keyup',handle_keyup);
    });
