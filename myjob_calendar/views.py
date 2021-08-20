from datetime import datetime
from myjob_calendar.forms import AddEventForm

from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.urls.base import reverse, reverse_lazy
from django.views.generic.edit import FormView

from myjob_calendar.models import Event
from myjob_calendar.utils.calendar import CustomCalendar
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.utils.safestring import mark_safe


class CalendarView(LoginRequiredMixin, TemplateView):
    """Calendar view"""

    template_name = "myjob_calendar/home.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        today = datetime.today()

        if 'month' in self.kwargs:
            month = self.kwargs['month']
        else:
            month = today.month
        if 'year' in self.kwargs:
            year = self.kwargs['year']
        else:
            year = today.year

        context['active_page'] = 'calendar'
        context["html_calendar"] = self.get_html_calendar(month, year)
        context['add_event_form'] = AddEventForm(self.request.user)

        return context

    def get_html_calendar(self, month, year):

        cal = CustomCalendar(year=year, month=month, user=self.request.user)

        html_cal = cal.formatmonth()

        return mark_safe(html_cal)


class AddEventFormView(FormView):
    template_name = 'myjob_calendar/form_add_event.html'
    form_class = AddEventForm
    success_url = reverse_lazy('calendar_home')

    def form_valid(self, form):

        form.add_event()

        return super().form_valid(form)

    def form_invalid(self, form):

        print('\n\nFORM INVALID\n\n')
        print(form)
        print('\n\nFORM INVALID\n\n')

        # error_message = self.format_error(form)
        # messages.error(self.request, error_message)

        return redirect(reverse('appliances_home'))

    def format_error(self, *args):

        message = 'An error occured :\n'

        for form in args:
            error_data = form.errors.as_data()
            for error_field, error_types in error_data.items():
                message += f'  {error_field} :\n'
                for list_error_type in error_types:
                    for error_message in list_error_type:
                        message += error_message

        return message


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
        start_time__gte=today
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


