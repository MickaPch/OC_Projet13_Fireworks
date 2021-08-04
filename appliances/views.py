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

class AppliancesHomeView(LoginRequiredMixin, TemplateView):
    """Appliances Home view"""

    template_name = "appliances/appliances.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        appliances = self.get_queryset_appliances()
        context['active_page'] = 'appliances'
        context["appliances"] = appliances
        # context["contacts"] = self.get_queryset_contacts(companies)
        # context["missions"] = self.get_queryset_missions(companies)

        return context

    def get_queryset_appliances(self):
        appliances = Appliance.objects.filter(
            company__user__in=[self.request.user.pk],
            user=self.request.user
        )

        return appliances

    # def get_queryset_contacts(self, companies):
    #     contacts = Contact.objects.filter(
    #         company__in=companies,
    #         user=self.request.user
    #     )

    #     return contacts

    # def get_queryset_missions(self, companies):
    #     missions = Mission.objects.filter(
    #         company__in=companies,
    #         user=self.request.user
    #     )

    #     return missions
