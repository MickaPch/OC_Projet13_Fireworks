function editCompany(btn) {

    if (btn.hasClass('btn-card-company-footer')) {
        var modal = $(btn.data('target'));
    } else {
        var modal = btn.closest('.modal-company');
    }

    var modal_footer = modal.find('.modal-footer');
    var row_edit_company = modal_footer.find('.row-edit-company');
    row_edit_company.addClass('display-none');

    var row_submit_company = modal_footer.find('.row-submit-company');
    row_submit_company.removeClass('display-none');

    var form = modal.find('form');

    var select_company = form.find('.select-company-type');
    select_company.prop('disabled', false);

    form.find('.modal-company-infos').addClass('display-none');
    form.find('.modal-company-edit').removeClass('display-none');

}

function resetCompany(element) {
    var modal_company = element.closest('.modal-company');

    var row_edit_company = modal_company.find('.row-edit-company');
    row_edit_company.removeClass('display-none');

    var row_submit_company = modal_company.find('.row-submit-company');
    row_submit_company.addClass('display-none');

    var form = modal_company.find('form');

    var select_company = form.find('.select-company-type');
    select_company.prop('disabled', true);

    form.find('.modal-company-infos').removeClass('display-none');
    form.find('.modal-company-edit').addClass('display-none');

}

$(document).on('click', '.btn-edit-company', function() {
    editCompany($(this));
});

$(document).on('click', '.btn-reset-company', function() {
    resetCompany($(this));
});

$(document).on('hidden.bs.modal', '.modal-company', function() {
    resetCompany($(this));
});

$(document).on('change', '.select-company-type', function() {
    var select_val = $(this).val();

    var company_icon = $(this).closest('.modal-title').find('.company-icon');
    console.log(company_icon);

    if (select_val == 'ESN') {
        company_icon.html('<i class="fas fa-desktop fa-2x"></i>');
    } else if (select_val == 'SOFT') {
        company_icon.html('<i class="fas fa-laptop-code fa-2x"></i>');
    } else if (select_val == 'ENG') {
        company_icon.html('<i class="fas fa-tools fa-2x"></i>');
    } else if (select_val == 'IND') {
        company_icon.html('<i class="fas fa-industry fa-2x"></i>');
    } else if (select_val == 'WEB') {
        company_icon.html('<i class="fas fa-wifi fa-2x"></i>');
    } else {
        company_icon.html('<i class="fas fa-building fa-2x"></i>');
    }

});