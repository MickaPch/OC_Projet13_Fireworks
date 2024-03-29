from django.db.models import fields
from appliances.models import Appliance, STATUS_CHOICES, Task
from django import forms

from accounts.models import User

class EditApplianceForm(forms.ModelForm):

    appliance_pk = forms.IntegerField()
    CHOICES = [
        (0, 'N/A'),
        (1, 'BAD'),
        (2, 'POOR'),
        (3, 'MEDIUM'),
        (4, 'GOOD'),
        (5, 'EXCELLENT'),
    ]
    environment_notation = forms.ChoiceField(
        choices=CHOICES,
        label="Environment",
        widget=forms.RadioSelect
    )
    values_notation = forms.ChoiceField(
        choices=CHOICES,
        label="Values",
        widget=forms.RadioSelect
    )
    evolution_notation = forms.ChoiceField(
        choices=CHOICES,
        label="Evolution",
        widget=forms.RadioSelect
    )
    knowledge_notation = forms.ChoiceField(
        choices=CHOICES,
        label="Knowledge",
        widget=forms.RadioSelect
    )
    management_notation = forms.ChoiceField(
        choices=CHOICES,
        label="Management",
        widget=forms.RadioSelect
    )
    advantages_notation = forms.ChoiceField(
        choices=CHOICES,
        label="Advantages",
        widget=forms.RadioSelect
    )
    notoriety_notation = forms.ChoiceField(
        choices=CHOICES,
        label="Notoriety",
        widget=forms.RadioSelect
    )
    office_notation = forms.ChoiceField(
        choices=CHOICES,
        label="Office",
        widget=forms.RadioSelect
    )

    def __init__(self, *args, **kwargs):
        super(EditApplianceForm, self).__init__(*args, **kwargs)
        self.fields['estimated_salary'].required = False
        self.fields['proposed_salary'].required = False
        self.fields['environment_notation'].required = False
        self.fields['environment_details'].required = False
        self.fields['values_notation'].required = False
        self.fields['values_details'].required = False
        self.fields['evolution_notation'].required = False
        self.fields['evolution_details'].required = False
        self.fields['knowledge_notation'].required = False
        self.fields['knowledge_details'].required = False
        self.fields['management_notation'].required = False
        self.fields['management_details'].required = False
        self.fields['advantages_notation'].required = False
        self.fields['advantages_details'].required = False
        self.fields['notoriety_notation'].required = False
        self.fields['notoriety_details'].required = False
        self.fields['office_notation'].required = False
        self.fields['office_details'].required = False

    class Meta:
        model = Appliance
        fields = [
            'status',
            'estimated_salary',
            'proposed_salary',
            'environment_notation',
            'environment_details',
            'values_notation',
            'values_details',
            'evolution_notation',
            'evolution_details',
            'knowledge_notation',
            'knowledge_details',
            'management_notation',
            'management_details',
            'advantages_notation',
            'advantages_details',
            'notoriety_notation',
            'notoriety_details',
            'office_notation',
            'office_details'
        ]

        widgets = {
            'appliance_pk': forms.HiddenInput(),
            'estimated_salary': forms.NumberInput(
                attrs={
                    'type':'number',
                    'class': 'form-control',
                    'step': '0.5',
                    'min': '10',
                    'max': '70',
                    "value": ""
                }
            ),
            'proposed_salary': forms.NumberInput(
                attrs={
                    'type':'number',
                    'class': 'form-control',
                    'step': '0.5',
                    'min': '10',
                    'max': '70',
                    "value": ""
                }
            ),
            'environment_details': forms.Textarea(
                attrs={
                    'class': 'form-control appliance-textarea',
                    'rows': 4
                }
            ),
            'values_details': forms.Textarea(
                attrs={
                    'class': 'form-control appliance-textarea',
                    'rows': 4
                }
            ),
            'evolution_details': forms.Textarea(
                attrs={
                    'class': 'form-control appliance-textarea',
                    'rows': 4
                }
            ),
            'knowledge_details': forms.Textarea(
                attrs={
                    'class': 'form-control appliance-textarea',
                    'rows': 4
                }
            ),
            'management_details': forms.Textarea(
                attrs={
                    'class': 'form-control appliance-textarea',
                    'rows': 4
                }
            ),
            'advantages_details': forms.Textarea(
                attrs={
                    'class': 'form-control appliance-textarea',
                    'rows': 4
                }
            ),
            'notoriety_details': forms.Textarea(
                attrs={
                    'class': 'form-control appliance-textarea',
                    'rows': 4
                }
            ),
            'office_details': forms.Textarea(
                attrs={
                    'class': 'form-control appliance-textarea',
                    'rows': 4
                }
            )
        }

    def edit_appliance(self):

        appliance = Appliance.objects.get(
            pk=self.cleaned_data['appliance_pk']
        )

        appliance.status = self.cleaned_data['status']
        appliance.estimated_salary = self.cleaned_data['estimated_salary']
        appliance.proposed_salary = self.cleaned_data['proposed_salary']
        appliance.environment_notation = self.cleaned_data['environment_notation']
        appliance.environment_details = self.cleaned_data['environment_details']
        appliance.values_notation = self.cleaned_data['values_notation']
        appliance.values_details = self.cleaned_data['values_details']
        appliance.evolution_notation = self.cleaned_data['evolution_notation']
        appliance.evolution_details = self.cleaned_data['evolution_details']
        appliance.knowledge_notation = self.cleaned_data['knowledge_notation']
        appliance.knowledge_details = self.cleaned_data['knowledge_details']
        appliance.management_notation = self.cleaned_data['management_notation']
        appliance.management_details = self.cleaned_data['management_details']
        appliance.advantages_notation = self.cleaned_data['advantages_notation']
        appliance.advantages_details = self.cleaned_data['advantages_details']
        appliance.notoriety_notation = self.cleaned_data['notoriety_notation']
        appliance.notoriety_details = self.cleaned_data['notoriety_details']
        appliance.office_notation = self.cleaned_data['office_notation']
        appliance.office_details = self.cleaned_data['office_details']

        appliance.save()


class EditApplianceStatusForm(forms.ModelForm):

    appliance_pk = forms.IntegerField()
    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget= forms.Select(
            attrs= {
                'class': "form-control appliance-status"
            }
        )
    )
    class Meta:
        model = Appliance
        fields = [
            'status'
        ]

        widgets = {
            'appliance_pk': forms.HiddenInput()
        }
    def edit_appliance_status(self):

        appliance = Appliance.objects.get(
            pk=self.cleaned_data['appliance_pk']
        )

        appliance.status = self.cleaned_data['status']

        appliance.save()


class AddTaskForm(forms.ModelForm):

    user_pk = forms.IntegerField()
    appliance_pk = forms.IntegerField()

    class Meta:
        model = Task
        fields = [
            'description',
            'done'
        ]

        widgets = {
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control task-textarea'
                }
            )
        }

    def add_task(self):
        user_pk = self.cleaned_data['user_pk']
        user = User.objects.get(pk=user_pk)

        appliance_pk = self.cleaned_data['appliance_pk']
        appliance = Appliance.objects.get(pk=appliance_pk)

        self.new_task = Task.objects.create(
            user=user,
            appliance=appliance,
            description=self.cleaned_data['description']
        )

        return self.new_task


class CheckTaskForm(forms.ModelForm):

    task_pk = forms.IntegerField()

    class Meta:
        model = Task
        fields = [
            'done'
        ]

        widgets = {
            'done': forms.CheckboxInput(
                attrs={
                    'class': 'col-1 form-check-input checkbox-task task-hover'
                }
            )
        }

    def edit_task_check(self):
        task_pk = self.cleaned_data['task_pk']
        task = Task.objects.get(pk=task_pk)

        task.done = self.cleaned_data['done']

        task.save()


class EditTaskForm(forms.ModelForm):

    task_pk = forms.IntegerField()

    class Meta:
        model = Task
        fields = [
            'description'
        ]

        widgets = {
            'description': forms.TextInput(
                attrs={
                    'class': 'col-10 form-control label-input-task task-hover display-none'
                }
            )
        }

    def edit_task_description(self):
        task_pk = self.cleaned_data['task_pk']
        task = Task.objects.get(pk=task_pk)

        task.description = self.cleaned_data['description']

        task.save()

