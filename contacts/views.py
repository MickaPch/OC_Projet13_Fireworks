"""Module user.views"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from contacts.models import Company
from contacts.forms import CompanyAddForm


class ContactsHomeView(LoginRequiredMixin, TemplateView):
    """Contacts Home view"""

    template_name = "contacts/contacts.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["contacts"] = self.get_queryset_contacts()
        context["company_form"] = self.get_company_form()

        return context

    def get_queryset_contacts(self):
        contacts = Company.objects.filter(user=self.request.user)

        return contacts

    def get_company_form(self):
        company_form = CompanyAddForm()

        return company_form
