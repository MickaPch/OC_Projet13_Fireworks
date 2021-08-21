"""Module user.views"""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, request
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from contacts.forms import (CompanyAddForm, EditCompanyForm, CompanyDeleteForm, AddContactForm, EditContactForm, DeleteContactForm)
from contacts.models.models import Company, Contact


class ContactsHomeView(LoginRequiredMixin, TemplateView):
    """Contacts Home view"""

    template_name = "contacts/contacts.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        companies = self.get_queryset_companies()
        context['active_page'] = 'contacts'
        context["companies"] = companies
        context["contacts"] = self.get_queryset_contacts(companies)
        # context["missions"] = self.get_queryset_missions(companies)

        return context

    def get_queryset_companies(self):
        companies = Company.objects.filter(user=self.request.user)

        return companies

    def get_queryset_contacts(self, companies):
        contacts = Contact.objects.filter(
            company__in=companies,
            user=self.request.user
        )

        return contacts

    # def get_queryset_missions(self, companies):
    #     missions = Mission.objects.filter(
    #         company__in=companies,
    #         user=self.request.user
    #     )

    #     return missions


class ContactsAddCompanyFormView(FormView):
    template_name = 'contacts/form_add_company.html'
    form_class = CompanyAddForm
    success_url = reverse_lazy('contacts_home')

    def form_valid(self, form):

        form.add_company(self.request.user)

        return super().form_valid(form)

    def form_invalid(self, form):

        error_message = self.format_error(form)

        messages.error(self.request, error_message)

        return redirect(reverse('contacts_home'))

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


class ContactsEditCompanyFormView(FormView):
    template_name = 'contacts/form_edit_company.html'
    form_class = EditCompanyForm
    success_url = reverse_lazy('contacts_home')

    def form_valid(self, form):

        form.edit_company()

        return super().form_valid(form)


    def form_invalid(self, form):

        error_message = self.format_error(form)
        print(form)
        print(error_message)

        messages.error(self.request, error_message)

        return redirect(reverse('contacts_home'))

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

class ContactsDeleteCompanyFormView(FormView):
    template_name = 'contacts/form_delete_company.html'
    form_class = CompanyDeleteForm
    success_url = reverse_lazy('contacts_home')

    def form_valid(self, form):

        form.delete_company(self.request.user)

        return super().form_valid(form)


class ContactsAddContactFormView(FormView):
    template_name = 'contacts/form_add_contact.html'
    form_class = AddContactForm
    success_url = reverse_lazy('contacts_home')

    def form_valid(self, form):

        form.add_contact(self.request.user)

        return super().form_valid(form)


    def form_invalid(self, form):

        error_message = self.format_error(form)

        messages.error(self.request, error_message)

        return redirect(reverse('contacts_home'))

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

class ContactsEditContactFormView(FormView):
    template_name = 'contacts/form_contact.html'
    form_class = EditContactForm
    success_url = reverse_lazy('contacts_home')

    def form_valid(self, form):

        form.edit_contact()

        return super().form_valid(form)


    def form_invalid(self, form):

        error_message = self.format_error(form)
        print(form)
        print(error_message)

        messages.error(self.request, error_message)

        return redirect(reverse('contacts_home'))

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

class ContactsDeleteContactFormView(FormView):
    template_name = 'contacts/form_delete_contact.html'
    form_class = DeleteContactForm
    success_url = reverse_lazy('contacts_home')

    def form_valid(self, form):

        form.delete_contact(self.request.user)

        return super().form_valid(form)

    def form_invalid(self, form):

        print(form)


        return super().form_valid(form)

# class ContactsAddMissionFormView(FormView):
#     template_name = 'contacts/form_add_mission.html'
#     form_class = MissionAddForm
#     success_url = reverse_lazy('contacts_home')

#     def form_valid(self, form):

#         form.add_mission(self.request.user)

#         return super().form_valid(form)
    
#     def form_invalid(self, form):

#         print(form)

#         return super().form_invalid(form)


# class ContactsDeleteMissionFormView(FormView):
#     template_name = 'contacts/form_delete_mission.html'
#     form_class = MissionDeleteForm
#     success_url = reverse_lazy('contacts_home')

#     def form_valid(self, form):

#         form.delete_mission(self.request.user)

#         return super().form_valid(form)
