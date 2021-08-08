function handlerIn(element) {
    element.removeClass('left-bar-hidden').addClass('left-bar-shown');
    var span_text = $(".left-text-icon");
    span_text.removeClass('left-text-icon-hidden').addClass('left-text-icon-shown');
    var app_section = $(".app-section");
    app_section.removeClass('app-section-left-hidden').addClass('app-section-left-shown');
    var top_row = $(".top-row");
    top_row.removeClass('top-row-left-hidden').addClass('top-row-left-shown');
}

function handlerOut(element) {
    element.removeClass('left-bar-shown').addClass('left-bar-hidden');
    var span_text = $(".left-text-icon");
    span_text.removeClass('left-text-icon-shown').addClass('left-text-icon-hidden');
    var app_section = $(".app-section");
    app_section.removeClass('app-section-left-shown').addClass('app-section-left-hidden');
    var top_row = $(".top-row");
    top_row.removeClass('top-row-left-shown').addClass('top-row-left-hidden');
}

$(document).on({
    mouseenter: function () {
        handlerIn($(this))
    },
    mouseleave: function () {
        handlerOut($(this))
    }
}, ".left-bar");
