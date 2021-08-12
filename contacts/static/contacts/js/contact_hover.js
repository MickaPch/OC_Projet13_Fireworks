function handlerInContact(element) {
    var contact_card = element.offsetParent()
    contact_card.addClass('contact-card-hover');
}

function handlerOutContact(element) {
    var contact_card = element.offsetParent()
    contact_card.removeClass('contact-card-hover');
}

$(document).on({
    mouseenter: function () {
        handlerInContact($(this))
    },
    mouseleave: function () {
        handlerOutContact($(this))
    }
}, ".contact-item");
