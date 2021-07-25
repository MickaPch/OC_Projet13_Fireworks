"""Module user.views"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from contacts.models import Company
from contacts.forms import CompanyAddForm


class ContactsHomeView(LoginRequiredMixin, TemplateView):
    """Contacts Home view"""

    template_name = "contacts/contacts.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["contacts"] = self.get_queryset_contacts()

        return context

    def get_queryset_contacts(self):
        contacts = Company.objects.filter(user=self.request.user)

        return contacts


class ContactsAddCompanyFormView(FormView):
    template_name = 'contacts/form_add_company.html'
    form_class = CompanyAddForm
    success_url = reverse_lazy('contacts_home')

    def form_valid(self, form):

        form.add_company(self.request.user)

        return super().form_valid(form)
