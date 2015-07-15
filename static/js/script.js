$(document).on('ready', function(){
    $('.card.alignment').on('click', function(){
        var data_id = $(this).data("id")
        $('.modal').filter('[data-id="'+data_id+'"]').modal('show');
    });
});