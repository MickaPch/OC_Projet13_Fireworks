function handlerInContact(element) {
    var contact_card = element.offsetParent()
    contact_card.addClass('contact-card-hover');
}

function handlerOutContact(element) {
    var contact_card = element.offsetParent()
    contact_card.removeClass('contact-card-hover');
}

function handlerInCard(element) {
    var contact_card = element.closest(".card-company");
    var company_infos = contact_card.find('.card-company-infos');
    var company_contacts = contact_card.find('.card-company-contacts');
    var company_fill = contact_card.find('.card-company-fill');
    var card_contact = contact_card.find('.card-contact');

    company_infos.addClass('card-company-hover');
    company_contacts.addClass('card-company-hover');
    company_fill.addClass('card-company-hover');
    card_contact.addClass('card-company-hover');
}

function handlerOutCard(element) {
    var contact_card = element.closest(".card-company");
    var company_infos = contact_card.find('.card-company-infos');
    var company_contacts = contact_card.find('.card-company-contacts');
    var company_fill = contact_card.find('.card-company-fill');
    var card_contact = contact_card.find('.card-contact');

    company_infos.removeClass('card-company-hover');
    company_contacts.removeClass('card-company-hover');
    company_fill.removeClass('card-company-hover');
    card_contact.removeClass('card-company-hover');
}



$(document).on({
    mouseenter: function () {
        handlerInContact($(this))
    },
    mouseleave: function () {
        handlerOutContact($(this))
    }
}, ".contact-item");


$(document).on({
    mouseenter: function () {
        handlerInCard($(this))
    },
    mouseleave: function () {
        handlerOutCard($(this))
    }
}, ".card-company-title");
