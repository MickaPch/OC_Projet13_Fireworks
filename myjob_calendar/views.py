from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse

from myjob_calendar.models import Event
from myjob_calendar.utils import CustomCalendar
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.safestring import mark_safe


class CalendarHomeView(LoginRequiredMixin, TemplateView):
    """Calendar Home view"""

    template_name = "myjob_calendar/home.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        # events = self.get_events()
        context['active_page'] = 'calendar'
        context["html_calendar"] = self.get_html_calendar()

        return context

    def get_html_calendar(self):

        today = datetime.today()

        cal = CustomCalendar(year=today.year, month=today.month, user=self.request.user)

        html_cal = cal.formatmonth()

        return mark_safe(html_cal)


@login_required
def get_events_day(request, day):

    date_req = day.split('-')

    events = Event.objects.filter(
        appliance__user=request.user,
        start_time__year=date_req[0],
        start_time__month=date_req[1],
        start_time__day=date_req[2],
    )

    if events.count() == 0:
        events_day = [{
            'badge_event': '',
            'get_time_formatted': '',
            'title': 'No event to show',
            'description': '',
            'date': ''
        }]
    else:
        events_day = []
        for event in events:
            events_day.append({
                'badge_event': event.get_badge(),
                'get_time_formatted': event.get_time_formatted(),
                'title': event.title,
                'description': event.description,
                'date': event.get_formatted_date()
            })


    return JsonResponse({
        'events': events_day
    })

@login_required
def get_events_to_come(request):

    today = datetime.today()

    events = Event.objects.filter(
        appliance__user=request.user,
        # start_time__gte=today
    ).order_by('start_time')


    if events.count() == 0:
        events_to_come = [{
            'badge_event': '',
            'get_time_formatted': '',
            'title': 'No event to show',
            'description': '',
            'date': ''
        }]
    else:
        events_to_come = []
        for event in events:
            events_to_come.append({
                'badge_event': event.get_badge(),
                'get_time_formatted': event.get_time_formatted(),
                'title': event.title,
                'description': event.description,
                'date': event.get_formatted_date()
            })

    return JsonResponse({
        'events': events_to_come
    })


