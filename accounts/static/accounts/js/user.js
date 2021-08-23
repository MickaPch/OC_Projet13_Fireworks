var enterPressed = false;
var focus_out = true;
var username = $('.user-username-link').html();

var active_element = document.activeElement;

$(document).on('focus', '.form-element', function() {
    focus_out = false;
    if ($(this).hasClass('btn-form-submit')) {
        focus_out = true;
    }
})

$(document).on('click', '.user-username-link', function() {
    $(this).addClass('display-none');
    var user_edit_form = $(this).parent().find('.user-username-form');
    user_edit_form.removeClass('display-none').addClass('display-inline');
    var user_edit_input = user_edit_form.find('.user-username-input');
    user_edit_input.val($(this).html()).focus();
    enterPressed = false

});

$(document).on('click', '.btn-name-edit', function() {
    $(this).addClass('display-none');
    var user_name = $(this).parent().find('.user-name');
    user_name.addClass('display-none');
    var form = $(this).parent().find('.user-name-form');
    form.removeClass('display-none').addClass('display-inline');
    var input_first_name = form.find('.user-first_name-input');
    input_first_name.focus();
    enterPressed = false

});

$(document).on('click', '.btn-email-edit', function() {
    $(this).addClass('display-none');
    var user_email = $(this).parent().find('.user-email');
    user_email.addClass('display-none');
    var form = $(this).parent().find('.user-email-form');
    form.removeClass('display-none').addClass('display-inline');
    var input_email = form.find('.user-email-input');
    input_email.focus();
    enterPressed = false

});


$(document).on('keydown', '.form-element', function(e) {
    var keyCode = e.keyCode || e.which; 
    enterPressed = (keyCode==13) ? true : false;
});

$(document).on('focusout', '.form-element', function(e) {
    e.preventDefault();
    var form = $(this).closest('form');

    if (!(enterPressed) && focus_out) {
        form.submit();
    }

});


$(document).on('submit', 'form', function(e) {
    e.preventDefault();

    var serializedData = $(this).serialize();

    if ($(this).data('type') == 'username') {
        var username_input = $('.user-username-input').val();
        var user_username_link = $(".user-username-link");

        user_username_link.html(username_input).removeClass('display-none');
        $(this).addClass('display-none').removeClass('display-inline');

    } else if ($(this).data('type') == 'name') {

        var user_name = $(".user-name");
        var first_name_input = $('.user-first_name-input').val();
        var user_first_name = user_name.find('.user-first_name');
        user_first_name.html(first_name_input);
        
        var last_name_input = $('.user-last_name-input').val();
        var user_last_name = user_name.find('.user-last_name');
        user_last_name.html(last_name_input);

        user_name.removeClass('display-none');

        $(this).addClass('display-none').removeClass('display-inline');

        var btn_name_edit = $(this).parent().find('.btn-name-edit');
        btn_name_edit.removeClass('display-none');

    } else if ($(this).data('type') == 'email') {

        var user_email = $(".user-email");
        var email_input = $('.user-email-input').val();
        user_email.html(email_input).removeClass('display-none');

        $(this).addClass('display-none').removeClass('display-inline');

        var btn_email_edit = $(this).parent().find('.btn-email-edit');
        btn_email_edit.removeClass('display-none');

    }


    if (username_input != username) {
        $.ajax({
            type: 'POST',
            url: $(this).data('url'),
            data: serializedData,
            success: function(response) {
                if ('username' in response) {
                    username = response['username'];
                }
            },
            error: function(response) {
                alert('error');
            }
        });
    }
    
});