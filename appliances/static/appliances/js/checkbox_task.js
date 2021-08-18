var form_type = "";

$(document).on('change', ".checkbox-task", function(e) {

    var checkbox = $(this);
    var task_input_text = $(this).parent().find(".label-task");

    if ( checkbox.is(':checked') ) {
        task_input_text.addClass('text-muted label-mute');
    } else {
        task_input_text.removeClass('text-muted label-mute');
    }

    var form = $(this).closest('.form-task');
    form_type = "check";
    form.submit()

});



$(document).on('click', ".btn-task-edit", function() {
    var btn_task_edit = $(this);

    var task_input_text = btn_task_edit.parent().find(".label-task");
    if (task_input_text.hasClass('display-reset')) {
        task_input_text.removeClass('display-reset');
    }
    task_input_text.addClass('display-none');
    

    var label_input_task = btn_task_edit.parent().find('.label-input-task');
    label_input_task.removeClass('display-none').addClass('display-reset').focus();

    if (btn_task_edit.hasClass('display-reset')) {
        btn_task_edit.removeClass('display-reset');
    }
    btn_task_edit.addClass('display-none');

    var btn_task_delete = btn_task_edit.parent().find(".btn-task-delete");
    if (btn_task_delete.hasClass('display-reset')) {
        btn_task_delete.removeClass('display-reset');
    }
    btn_task_delete.addClass('display-none');

});


$(document).on('click', ".btn-task-delete", function() {

    var task_pk = $(this).data('task_pk');

    var endpoint = '/appliances/delete_task/' + task_pk;

    $.ajax({
        url: endpoint,
        type: "GET",
        dataType: "json",
        success: function(response) {
            var task_pk = response['task_pk'];
            var row_id = "#row_task_" + task_pk

            $(row_id).remove();

            var appliance_task_count = "#appliance_task_count_" + response['appliance_pk'];
            var new_task_count = response['appliance_task_count'];
            $(appliance_task_count).html(new_task_count);
        },
        error: function(response) {
            alert('error');
        }
    });


});

$(document).on('focusout', '.label-input-task', function() {
    var new_text_task = $(this).val();

    var task_input_text = $(this).parent().find(".label-task");
    task_input_text.text(new_text_task).removeClass('display-none').addClass('display-reset');

    var btn_task_edit = $(this).parent().find(".btn-task-edit");
    btn_task_edit.removeClass('display-none').addClass('display-reset');

    var btn_task_delete = $(this).parent().find(".btn-task-delete");
    btn_task_delete.removeClass('display-none').addClass('display-reset');

    if ($(this).hasClass('display-reset')) {
        $(this).removeClass('display-reset');
    }
    $(this).addClass('display-none');

    var form = $(this).closest('.form-task');
    form_type = "description";
    form.submit()

});


$(document).on('submit', '.form-task', function(e) {
    e.preventDefault();

    var serializedData = $(this).serialize();

    if (form_type == 'check') {
        $.ajax({
            type: 'POST',
            url: $(this).data('urlcheck'),
            data: serializedData,
            success: function(response) {
                var appliance_pk = response['appliance_pk'];
                var appliance_task_count = "#appliance_task_count_" + appliance_pk;
                var new_task_count = response['appliance_task_count'];
                $(appliance_task_count).html(new_task_count);
            },
            error: function(response) {
                alert('error');
            }
        });
    } else if ( form_type == "description" ) {
        $.ajax({
            type: 'POST',
            url: $(this).data('urldescription'),
            data: serializedData,
            success: function(response) {
            },
            error: function(response) {
                alert('error');
            }
        });
    } else {
        alert('error in AJAX send')
    }
    
});