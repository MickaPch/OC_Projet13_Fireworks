$(document).on('click', '.event-item', function(e) {
    e.preventDefault();

    console.log($(this));
    console.log('click to open event');
});


function handlerInVerticalCol(element) {
    element.addClass('col-vertical-hover');
}

function handlerOutVerticalCol(element) {
    element.removeClass('col-vertical-hover');
}

function clickVerticalCol(element) {
    element.addClass('display-none').removeClass('display-reset');
    var col_events_to_display = $(".col-events-to-display");
    col_events_to_display.removeClass('display-none animateout').addClass('display-reset animatein');
    $(".calendar-full").addClass('animatein').removeClass('animateout');

    var col_name = $(".col-events-to-display").find('.col-events-title');
    col_name.html('Events to come');

    $(".vertical-timeline").html('');

    $.ajax({
        url: element.data('url'),
        type: "GET",
        dataType: "json",
        success: (response) => {
            for (const event of response['events']) {
                $(".vertical-timeline").append(formatDiv(event));
            }
        },
        error: (response) => {console.log('error');}
    });


}

function formatDiv(event) {
    return div = `
<div class="vertical-timeline-item vertical-timeline-element">
    <div> <span class="vertical-timeline-element-icon bounce-in"> <i class="badge badge-timeline ` + event['badge_event'] + `"></i> </span>
        <div class="vertical-timeline-element-content bounce-in">
            <div class="timeline-title">` + event['get_time_formatted'] + ` ` + event['title'] + `</div>
            <p>` + event['description'] + `</p> <span class="vertical-timeline-element-date">` + event['date'] + `</span>
        </div>
    </div>
</div>`

}

function showEventItemsThisDay(element) {
    $(".col-vertical").addClass('display-none').removeClass('display-reset');
    
    var col_events_to_display = $(".col-events-to-display");
    col_events_to_display.removeClass('display-none animateout').addClass('display-reset animatein');
    $(".calendar-full").addClass('animatein').removeClass('animateout');

    var col_name = $(".col-events-to-display").find('.col-events-title');

    var month_year = $('.month').html().split(' ');
    var date_string = month_year[0] + " " + element.find('.date').html() + ", " + month_year[1]
    col_name.html(date_string);
    $(".vertical-timeline").html('');

    $.ajax({
        url: element.data('url'),
        type: "GET",
        dataType: "json",
        success: (response) => {
            for (const event of response['events']) {
                $(".vertical-timeline").append(formatDiv(event));
            }
        },
        error: (response) => {console.log('error');}
    });

}

$(document).on({
    mouseenter: function () {
        handlerInVerticalCol($(this))
    },
    mouseleave: function () {
        handlerOutVerticalCol($(this))
    },
    click: function () {
        clickVerticalCol($(this))
    }
}, ".col-vertical");

$(document).on('click', '.close-event-timeline', function() {
    var col_events_display_none = $(".col-events-to-come, .col-events-to-display");
    col_events_display_none.addClass('animateout').removeClass('display-reset animatein');
    $(".calendar-full").removeClass('animatein');
    setTimeout(() => { 
        col_events_display_none.addClass('display-none');
        $(".col-vertical").removeClass('display-none').addClass('display-reset');
    }, 600); 
});

$(document).on({
    click: function () {
        showEventItemsThisDay($(this))
    }
}, ".day");
