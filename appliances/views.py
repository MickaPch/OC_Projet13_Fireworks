"""Module user.views"""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, request
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from appliances.models import Appliance
from appliances.forms import EditApplianceForm

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
        )

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
        print(form)
        print(error_message)

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
