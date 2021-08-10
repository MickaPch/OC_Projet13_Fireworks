$(document).ready(function() {
    
    $(".contact-phonenumber").each(function() {
        var phonenumber_array = Array.from($(this).html());

        var phonenumber_temp = new Array;        

        for (var i = 0; i < phonenumber_array.length; i += 2) {
            phonenumber_temp.push(phonenumber_array.slice(i, i + 2).join(''));
        }

        phonenumber = new String;
        for (var phone_elem of phonenumber_temp) {
            phonenumber = phonenumber + '<span class="mr-1">' + phone_elem + '</span>'
        }

        $(this).html(phonenumber);
    });

});