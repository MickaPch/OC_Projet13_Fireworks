$(document).ready(function() {
    
    $(".business-list").each(function() {
        var business_list = $(this).html().split('---');

        business = new String;
        for (var business_elem of business_list) {
            icon_list = business_elem.split('///');
            business = business + '<i class="' + icon_list[1] + ' fa-2x mr-4" title="' + icon_list[0] + '"></i>'
        }

        $(this).html(business);
    });

});