from datetime import datetime
from calendar import HTMLCalendar, month_name

from django.urls.base import reverse
from myjob_calendar.models import Event
from myjob_calendar.utils.time import format_time


class CustomCalendar(HTMLCalendar):

    def __init__(self, year=None, month=None, user=None):
        self.year = year
        self.month = month
        self.user = user
        super(CustomCalendar, self).__init__()
    
    def formatday(self, day, events):

        events_this_day = events.filter(start_time__day=day)

        day_events = str()
        for event in events_this_day[:2]:

            event_badge = event.get_badge_bg()

            hour = format_time(event.start_time.hour)
            minutes = format_time(event.start_time.minute)

            event_time = f"{hour}:{minutes}"

            day_events += f'<li class="event row align-items-center"><div class="event-item {event_badge} mb-1">{event_time} {event.title}</div></li>'

        if len(events_this_day) > 2:
            nb_others = len(events_this_day) - 2

            day_events += f'<li class="event row mt-2"><div class="event-item-others badge badge-light mb-1">{str(nb_others)} others ...</div></li>'

        if day != 0:
            today = datetime.today().day
            if day < today:
                class_day = "past"
            elif day == today:
                class_day = "today"
            else:
                class_day = "future"

            month = format_time(self.month)
            format_day = format_time(day)

            str_day = str(self.year) + "-" + month + "-" + format_day
            url_get_events = reverse('get_events_day', kwargs={'day': str_day})

            return f'<td class="{class_day} day" data-url="{url_get_events}"><a class="date" href="#" data-toggle="modal" data-target="#modal_event">{day}</a><div class="date-format display-none">{str_day}</div><ul class="event-list">{day_events}</ul></td>'

        return "<td class='noday'></td>"
    
    def formatweek(self, theweek, events):
        
        week = str()
        for day, weekday in theweek:
            week += self.formatday(day, events)
        
        return f"<tr>{week}</tr>"

    def formatmonthname(self, theyear, themonth, withyear=True):
        """
        Return a month name as a table row.
        """
        if withyear:
            s = '%s %s' % (month_name[themonth], theyear)
        else:
            s = '%s' % month_name[themonth]
        


        format_month_name = '<tr class="month-tr container-fluid">' # open tr
        format_month_name += f'<th colspan="7" class="{self.cssclass_month_head}">' # open th
        format_month_name += '<div class="row align-items-center justify-content-between">' # open row

        previous_month = themonth - 1
        url_previous_month = reverse('month_view', kwargs={'month': previous_month, 'year': theyear})
        format_month_name += f'<a class="col-2 link-month" href="{url_previous_month}">'
        format_month_name += '<i class="fas fa-chevron-left"></i></a>'
        format_month_name += f'<div class="col-4 month-title">{s}</div>'

        next_month = themonth + 1
        url_next_month = reverse('month_view', kwargs={'month': next_month, 'year': theyear})
        format_month_name += f'<a class="col-2 link-month" href="{url_next_month}">'
        format_month_name += '<i class="fas fa-chevron-right"></i></a>'

        format_month_name += '</div>' # close row
        format_month_name += '</th>' # close th
        format_month_name += '</tr>' # close tr

        return format_month_name

    def formatweekheader(self):
        """
        Return a header for a week as a table row.
        """
        s = ''.join(self.formatweekday(i) for i in self.iterweekdays())
        return '<tr class="weekday-tr">%s</tr>' % s

    def formatmonth(self, withyear=True):

        events = Event.objects.filter(
            appliance__user__in=[self.user.pk],
            start_time__year=self.year,
            start_time__month=self.month
        )

        html_cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        html_cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        html_cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            html_cal += f'{self.formatweek(week, events)}\n'
        html_cal += '</table>'

        return html_cal
