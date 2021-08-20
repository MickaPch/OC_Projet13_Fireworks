from appliances.models import Appliance
from myjob_calendar.models import Event
from django import forms
from django.utils.translation import ugettext_lazy as _


class AddEventForm(forms.ModelForm):

    type = forms.ChoiceField(
        choices=Event.TYPES,
        label="Type",
        widget=forms.Select
    )

    def __init__(self, user=None, *args, **kwargs):
        super(AddEventForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False
        self.fields['end_time'].required = False

        if user is not None:
            self.fields['appliance'].queryset = self.get_user_appliances(user)

    class Meta:
        model = Event
        fields = [
            'title',
            'description',
            'type',
            'start_time',
            'end_time',
            'appliance'
        ]

        widgets = {
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control appliance-textarea',
                    'rows': 4
                }
            ),
            'start_time': forms.DateTimeInput(
                attrs={
                    'class': 'form-control datetimepicker-input',
                    'data-target': '#datetimepicker_start'
                }
            ),
            'end_time': forms.DateTimeInput(
                attrs={
                    'class': 'form-control datetimepicker-input',
                    'data-target': '#datetimepicker_end'
                }
            )
        }

        labels = {
            "start_time": _("Start time"),
        }

    def add_event(self):

        event = Event.objects.create(
            appliance=self.cleaned_data['appliance'],
            title=self.cleaned_data['title'],
            description=self.cleaned_data['description'],
            type=self.cleaned_data['type'],
            start_time=self.cleaned_data['start_time'],
            end_time=self.cleaned_data['end_time']
        )
        event.save()

    def get_user_appliances(self,user):

        appliances_queryset = Appliance.objects.filter(user=user)

        return appliances_queryset
