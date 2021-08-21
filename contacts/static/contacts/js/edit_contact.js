function editContact(btn) {
    var modal_footer = btn.closest('.modal-footer');
    var row_edit_contact = modal_footer.find('.row-edit-contact');
    row_edit_contact.addClass('display-none');

    var row_submit_contact = modal_footer.find('.row-submit-contact');
    row_submit_contact.removeClass('display-none');

    var form = btn.closest('form');

    var select_company = form.find('.contact-company');
    select_company.prop('disabled', false);

    form.find('.modal-contact-infos').addClass('display-none');
    form.find('.modal-contact-form-edit').removeClass('display-none');

}

function resetContact(element) {
    var modal_contact = element.closest('.modal-contact');

    var row_edit_contact = modal_contact.find('.row-edit-contact');
    row_edit_contact.removeClass('display-none');

    var row_submit_contact = modal_contact.find('.row-submit-contact');
    row_submit_contact.addClass('display-none');

    var form = modal_contact.find('form');

    var select_company = form.find('.contact-company');
    select_company.prop('disabled', true);

    form.find('.modal-contact-infos').removeClass('display-none');
    form.find('.modal-contact-form-edit').addClass('display-none');

}

$(document).on('click', '.btn-edit-contact', function() {
    editContact($(this));
});

$(document).on('click', '.btn-reset-contact', function() {
    resetContact($(this));
});

$(document).on('hidden.bs.modal', '.modal-contact', function() {
    resetContact($(this));
});