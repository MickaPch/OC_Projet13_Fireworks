// $(function() {
//     $('#ButtonEnvironmentPopover').popover(
//         {
//             title: 'Environment details',
//             container: '.modal-edit-appliance',
//             html: true,
//             placement: 'bottom',
//             sanitize: false,
//             content: `
//                     <div class="input-group">
//                         <textarea class="form-control" rows="3" id="textarea_environment_details"></textarea>
//                         <button class="btn btn-outline-primary" type="button" data-toggle="popover" data-placement="bottom"
//                             data-html="true" data-title="Search">
//                             <i class="fas fa-search"></i>
//                         </button>
//                     </div>`
//         }
//     );
// });

// $(function() {
//     $("#textarea_environment_details").on('keyup', function() {
//         console.log($(this).val());
//     });
    
// });

$("[data-toggle=popover]").each(function( index ) {

    var that = $(this);
    var container_id = '#modal_edit_appliance_' + $(this).attr('id').slice(-1);
    $(this).popover({
        container: container_id,
        html: true,
        placement: 'bottom',
        content: function () {
            return $('#' + $(this).attr('id') + ' + .popoverContent').html();
        }
    });
});

$('[data-toggle=popover]').on('shown.bs.popover', function () {
    console.log($('#' + $(this).attr('aria-describedby') + ' .popover-body .input-group textarea'));
    $('#' + $(this).attr('aria-describedby') + ' .popover-body .input-group textarea').focus();
});

$('[data-toggle=popover]').on('hide.bs.popover', function () {
    $('#' + $(this).attr('id') + ' + .popoverContent textarea').html( $('#' + $(this).attr('aria-describedby') + ' .popover-body .input-group textarea').val());
});