"""Module user.views"""
from appliances.charts import BACKGROUND_COLOR, BORDER_COLOR
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg
from django.http import HttpResponseRedirect, request
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.http.response import JsonResponse

from appliances.models import Appliance, NOTATIONS_LABELS, Task
from appliances.forms import AddTaskForm, CheckTaskForm, EditApplianceForm, EditApplianceStatusForm, EditTaskForm

class AppliancesHomeView(LoginRequiredMixin, TemplateView):
    """Appliances Home view"""

    template_name = "appliances/appliances.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        appliances = self.get_queryset_appliances()
        context['active_page'] = 'appliances'
        context["appliances"] = appliances

        return context

    def get_queryset_appliances(self):
        appliances = Appliance.objects.filter(
            company__user__in=[self.request.user.pk],
            user=self.request.user
        ).order_by('status')

        return appliances


class EditApplianceFormView(FormView):
    template_name = 'appliances/form_edit_appliance.html'
    form_class = EditApplianceForm
    success_url = reverse_lazy('appliances_home')

    def form_valid(self, form):

        form.edit_appliance()

        return super().form_valid(form)


    def form_invalid(self, form):

        error_message = self.format_error(form)

        messages.error(self.request, error_message)

        return redirect(reverse('appliances_home'))

    def format_error(self, *args):

        message = str()

        for form in args:
            error_data = form.errors.as_data()
            for error_field, error_types in error_data.items():
                message += f'  {error_field} :\n'
                for list_error_type in error_types:
                    for error_message in list_error_type:
                        message += error_message

        return message

class EditApplianceStatusFormView(FormView):
    template_name = 'appliances/form_appliance_status.html'
    form_class = EditApplianceStatusForm
    success_url = reverse_lazy('appliances_home')

    def form_valid(self, form):

        form.edit_appliance_status()

        return super().form_valid(form)


    def form_invalid(self, form):

        print(form)
        error_message = self.format_error(form)

        messages.error(self.request, error_message)

        return redirect(reverse('appliances_home'))

    def format_error(self, *args):

        message = str()

        for form in args:
            error_data = form.errors.as_data()
            for error_field, error_types in error_data.items():
                message += f'  {error_field} :\n'
                for list_error_type in error_types:
                    for error_message in list_error_type:
                        message += error_message

        return message

class AddTaskFormView(FormView):
    template_name = 'appliances/form_add_task.html'
    form_class = AddTaskForm
    success_url = reverse_lazy('appliances_home')

    def form_valid(self, form):

        print('form valid')

        form.add_task()

        return super().form_valid(form)

    def form_invalid(self, form):

        error_message = self.format_error(form)

        messages.error(self.request, error_message)

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


class CheckTaskFormView(FormView):
    template_name = 'appliances/checkbox_task.html'
    form_class = CheckTaskForm
    success_url = reverse_lazy('appliances_home')

    def form_valid(self, form):

        form.edit_task()

        return super().form_valid(form)

    def form_invalid(self, form):

        print('\n\nFORM INVALID\n\n')
        print(form)
        print('\n\nFORM INVALID\n\n')

        error_message = self.format_error(form)

        messages.error(self.request, error_message)

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

class EditTaskFormView(FormView):
    template_name = 'appliances/checkbox_task.html'
    form_class = EditTaskForm
    success_url = reverse_lazy('appliances_home')

    def form_valid(self, form):

        form.edit_task()

        return super().form_valid(form)

    def form_invalid(self, form):

        print('\n\nFORM INVALID\n\n')
        print(form)
        print('\n\nFORM INVALID\n\n')

        error_message = self.format_error(form)

        messages.error(self.request, error_message)

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
def check_task(request):

    form = CheckTaskForm(request.POST)

    if form.is_valid():
        form.edit_task_check()
        task_pk = form.cleaned_data['task_pk']
        task = Task.objects.get(pk=task_pk)
    else:
        print(form)
    

    return JsonResponse({
        'task_pk': task_pk,
        'appliance_pk': task.appliance.pk,
        'appliance_task_count': task.appliance.get_tasks_count()
    })


@login_required
def edit_task_description(request):

    form = EditTaskForm(request.POST)

    if form.is_valid():
        form.edit_task_description()
        task_pk = form.cleaned_data['task_pk']
        task = Task.objects.get(pk=task_pk)
    else:
        print(form)

    return JsonResponse({
        'task_pk': task_pk,
        'appliance_pk': task.appliance.pk
    })

@login_required
def add_task_input(request, appliance_pk):

    form = AddTaskForm(request.POST)

    task_pk = ""

    if form.is_valid():
        task = form.add_task()
        task_pk = task.pk


        return JsonResponse({
            'task_pk': task_pk,
            'task_description': task.description,
            'task_done': task.done,
            'appliance_task_count': task.appliance.get_tasks_count()
        })

    else:
        print('INVALID FORM')
        print(form)


@login_required
def delete_task(request, task_pk):

    task = Task.objects.get(pk=task_pk)
    appliance_pk = task.appliance.pk

    task.delete()

    appliance = Appliance.objects.get(pk=appliance_pk)
    appliance_task_count = appliance.get_tasks_count()

    return JsonResponse({
        'task_pk': task_pk,
        'appliance_pk': appliance_pk,
        'appliance_task_count': appliance_task_count
    })


@login_required
def get_notations_chart(request, appliance_pk):

    appliance = Appliance.objects.get(pk=appliance_pk)

    return JsonResponse({
            'title': f'Notations for {appliance.company.name}',
            'data': {
                'labels': NOTATIONS_LABELS,
                'datasets': [{
                    'label': f'{appliance.company.name} notes (/5)',
                    'backgroundColor': BACKGROUND_COLOR,
                    'borderColor': BORDER_COLOR,
                    'data': appliance.get_notations_list()
                }]
            }
        })
