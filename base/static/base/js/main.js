function handlerInLeftBar() {
    var element = $('.leftbar');
    element.removeClass('leftbar-hidden').addClass('leftbar-shown');
    var span_text = $(".text-icon-leftbar");
    span_text.removeClass('text-icon-hidden').addClass('text-icon-shown');
    var footer_btn_group = $(".footer-btn-leftbar");
    footer_btn_group.removeClass('leftbar-hidden').addClass('leftbar-shown');
    // var app_section = $(".app-section");
    // app_section.removeClass('app-section-left-hidden').addClass('app-section-left-shown');
    // var top_row = $(".top-row");
    // top_row.removeClass('top-row-left-hidden').addClass('top-row-left-shown');
}

function handlerOutLeftBar() {
    var element = $('.leftbar');
    element.removeClass('leftbar-shown').addClass('leftbar-hidden');
    var span_text = $(".text-icon-leftbar");
    span_text.removeClass('text-icon-shown').addClass('text-icon-hidden');
    var footer_btn_group = $(".footer-btn-leftbar");
    footer_btn_group.removeClass('leftbar-shown').addClass('leftbar-hidden');
    // var app_section = $(".app-section");
    // app_section.removeClass('app-section-left-shown').addClass('app-section-left-hidden');
    // var top_row = $(".top-row");
    // top_row.removeClass('top-row-left-shown').addClass('top-row-left-hidden');
}

$(document).on({
    mouseenter: function () {
        handlerInLeftBar()
    },
    mouseleave: function () {
        handlerOutLeftBar()
    }
}, ".show-leftbar");

function handlerInUser(element) {
    var username = $(".topbar-username");
    username.removeClass('username-hidden').addClass('username-shown');
}

function handlerOutUser(element) {
    var username = $(".topbar-username");
    username.addClass('username-hidden').removeClass('username-shown');
}

$(document).on({
    mouseenter: function () {
        handlerInUser($(this))
    },
    mouseleave: function () {
        handlerOutUser($(this))
    }
}, ".topbar-profile");


function handlerInAdd() {
    var add_btn = $(".add-button-group");
    add_btn.removeClass('add-button-group-hidden').addClass('add-button-group-shown');
    var nav_item_footer_btn = $(".footer-btn-leftbar");
    nav_item_footer_btn.addClass('footer-btn-leftbar-hover');
}

function handlerOutAdd() {
    var add_btn = $(".add-button-group");
    add_btn.addClass('add-button-group-hidden').removeClass('add-button-group-shown');
    var nav_item_footer_btn = $(".footer-btn-leftbar");
    nav_item_footer_btn.removeClass('footer-btn-leftbar-hover');
}

$(document).on({
    mouseenter: function () {
        handlerInAdd()
    },
    mouseleave: function () {
        handlerOutAdd()
    }
}, ".show-add-btn");
