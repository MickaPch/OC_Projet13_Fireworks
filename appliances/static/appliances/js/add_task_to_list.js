function add_task_to_list(form, csrf_token, appliance_pk, url_check, url_description) {
    
    var serializedData = form.serialize();
    $.ajax({
        type: 'POST',
        url: form.data('url'),
        data: serializedData,
        success: function(response) {

            var task_list_appliance_id = "#task_list_" + appliance_pk;
            
            var task_done = response['task_done'];

            if (task_done) {
                var class_task_done = "text-muted label-mute"
            }

            var new_row_task = `
<div class="row w-100" id="row_task_` + response['task_pk'] + `">

<form method="post" class="edit-task form-task w-100" data-urlcheck="` + url_check + `" data-urldescription="` + url_description + `">
    ` + csrf_token + `

    <div class="form-group form-check container-fluid align-items-center">
        <div class="row justify-content-center">
            <div class="col-8">
                <div class="row align-items-center">
                    <div class='col-1'>
                    </div>
                    <div class='col-10 col-label col-display'>
                        <div class="input-task-text align-items-center justify-content-start">
                            <input type="hidden" name="task_pk" value="` + response['task_pk'] + `" id="form_check_task_task_pk_` + response['task_pk'] + `">
                            <input type="checkbox" name="done" class="col-1 form-check-input checkbox-task task-hover" id="form_check_task_done_` + response['task_pk'] + `">
                            <label class="col-9 form-check-label task-hover label-task ` + class_task_done + `" for="form_check_task_done_` + response['task_pk'] + `">
                                ` + response['task_description'] + `
                            </label>
                            <input type="hidden" name="task_pk" value="` + response['task_pk'] + `" id="form_description_task_task_pk_` + response['task_pk'] + `">
                            <input type="text" name="description" value="` + response['task_description'] + `" class="col-10 form-control label-input-task task-hover display-none" maxlength="255" required="" id="form_description_task_description_` + response['task_pk'] + `">
                            <button class="col-1 btn-reset btn-task btn-task-edit text-info" type="button" name="btn_edit_task">
                                <i class="fas fa-pencil-alt"></i>
                            </button>
                            <button class="col-1 btn-reset btn-task btn-task-delete text-danger" type="button" name="btn_delete_task" data-task_pk="` + response['task_pk'] + `">
                                <i class="fas fa-times"></i>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</form>

</div>
            `;


            $(task_list_appliance_id).append(new_row_task);

            var appliance_task_count = "#appliance_task_count_" + appliance_pk;
            var new_task_count = response['appliance_task_count'];
            $(appliance_task_count).html(new_task_count);
            $(".task-textarea").val('');

        },
        error: function(response) {
            alert('error');
        }
    });
    
}