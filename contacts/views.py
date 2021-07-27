"""Module user.views"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from contacts.models import Company, ContactMember, Mission
from contacts.forms import CompanyAddForm, ContactMemberAddForm, MissionAddForm, MissionDeleteForm


class ContactsHomeView(LoginRequiredMixin, TemplateView):
    """Contacts Home view"""

    template_name = "contacts/contacts.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        companies = self.get_queryset_companies()
        context["companies"] = companies
        context["contacts"] = self.get_queryset_contacts(companies)
        context["missions"] = self.get_queryset_missions(companies)

        return context

    def get_queryset_companies(self):
        companies = Company.objects.filter(user=self.request.user)

        return companies

    def get_queryset_contacts(self, companies):
        contacts = ContactMember.objects.filter(company__in=companies)

        return contacts

    def get_queryset_missions(self, companies):
        missions = Mission.objects.filter(
            company__in=companies,
            user=self.request.user
        )

        return missions


class ContactsAddCompanyFormView(FormView):
    template_name = 'contacts/form_add_company.html'
    form_class = CompanyAddForm
    success_url = reverse_lazy('contacts_home')

    def form_valid(self, form):

        form.add_company(self.request.user)

        return super().form_valid(form)

class ContactsAddContactMemberFormView(FormView):
    template_name = 'contacts/form_add_contact_member.html'
    form_class = ContactMemberAddForm
    success_url = reverse_lazy('contacts_home')

    def form_valid(self, form):

        form.add_contact_member()

        return super().form_valid(form)

class ContactsAddMissionFormView(FormView):
    template_name = 'contacts/form_add_mission.html'
    form_class = MissionAddForm
    success_url = reverse_lazy('contacts_home')

    def form_valid(self, form):

        form.add_mission(self.request.user)

        return super().form_valid(form)

class ContactsDeleteMissionFormView(FormView):
    template_name = 'contacts/form_delete_mission.html'
    form_class = MissionDeleteForm
    success_url = reverse_lazy('contacts_home')

    def form_valid(self, form):

        form.delete_mission(self.request.user)

        return super().form_valid(form)
