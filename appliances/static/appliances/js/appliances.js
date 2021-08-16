$(document).ready(function() {
    $(function () {
        $('[data-toggle="popover"]').popover()
    });
    $("[data-toggle=popover]").each(function( index ) {

        var that = $(this);
        var popover_content = $('#' + that.attr('id') + ' + .popoverContent').html()
        // console.log(popover_content);
        var container_id = '#modal_edit_appliance_' + $(this).attr('id').slice(-1);
        $(this).popover({
            container: container_id,
            html: true,
            placement: 'bottom',
            content: function () {
                console.log(that)
                return popover_content;
            }
        });
    });
    
    $('[data-toggle=popover]').on('shown.bs.popover', function () {
        $('#' + $(this).attr('aria-describedby') + ' .popover-body .input-group textarea').focus();
    });
    
    $('[data-toggle=popover]').on('hide.bs.popover', function () {
        var value = $('#' + $(this).attr('aria-describedby') + ' .popover-body .input-group textarea').val();
        var form_textarea = $('#' + $(this).attr('id') + ' + .popoverContent textarea');
        form_textarea.html(value);
        form_textarea.val(value);
    });

    $(".appliance-status").on('change', function() {
        var form = $(this).closest('form');
        form.submit()
    })

});