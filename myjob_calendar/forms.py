from myjob_calendar.models import Event
from django import forms


class AddEventForm(forms.ModelForm):

    appliance_pk = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super(AddEventForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False

    class Meta:
        model = Event
        fields = [
            'title',
            'description',
            'date',
            'type'
        ]

        widgets = {
            'appliance_pk': forms.HiddenInput(),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control appliance-textarea',
                    'rows': 4
                }
            )
        }

    def add_event(self):

        event = Event.objects.create(
            appliance=self.cleaned_data['appliance_pk'],
            title=self.cleaned_data['title'],
            description=self.cleaned_data['description'],
            type=self.cleaned_data['type'],
            date=self.cleaned_data['date']
        )
        event.save()
