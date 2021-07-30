"""Module user.views"""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, request
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from contacts.forms import (CompanyAddForm, ContactMemberAddForm,
                            MissionAddForm, MissionDeleteForm,
                            PhoneNumberAddForm)
from contacts.models.models import Company, ContactMember, Mission


class ContactsHomeView(LoginRequiredMixin, TemplateView):
    """Contacts Home view"""

    template_name = "contacts/contacts.html"

    def setup(self, request, *args, **kwargs):

        request.session = self.check_session(request.session)

        return super().setup(request, *args, **kwargs)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        companies = self.get_queryset_companies()
        context["companies"] = companies
        context["contacts"] = self.get_queryset_contacts(companies)
        context["missions"] = self.get_queryset_missions(companies)

        return context

    def check_session(self, session):

        if 'session_count' in session:
            if (
                'data' in session
                and session['session_count'] >= 2
            ):
                session['session_count'] = 0
                del session['data']
            elif 'data' in session:
                session['session_count'] += 1
        elif 'data' in session:
            session['session_count'] = 1
        
        return session


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

    def form_invalid(self, form):

        if 'data' not in self.request.session:
            self.request.session['data'] = {
                'add_company_form': {
                    'errors': form.errors.as_json(),
                    'data': form.cleaned_data
                }
            }
        else:
            self.request.session['data']['add_company_form'] = {
                'errors': form.errors.as_json(),
                'data': form.cleaned_data
            }

        return redirect(reverse('contacts_home'))


class ContactsAddContactMemberFormView(FormView):
    template_name = 'contacts/form_add_contact_member.html'
    form_class = ContactMemberAddForm
    success_url = reverse_lazy('contacts_home')

    def get_phone_form(self):
        if self.request.method == 'POST':
            return PhoneNumberAddForm(self.request.POST)
        else:
            return PhoneNumberAddForm()

    def form_valid(self, form):

        self.phone_form = self.get_phone_form()
        contact = form.add_contact_member()

        if self.phone_form.is_valid():
            self.phone_form.add_phone_number(contact)
            messages.success(self.request, 'Contact registered.')

            return super().form_valid(form)
        else:
            return self.form_invalid(form)
        
    def form_invalid(self, form):

        print(form.errors)
        print(self.phone_form.errors)

        error_message = self.format_error(form, self.phone_form)

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



        print()
        print(self.phone_form.errors.as_data())


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['phone_number_form'] = getattr(self, 'phone_number_form', self.get_phone_form())
    #     return context


class ContactsAddMissionFormView(FormView):
    template_name = 'contacts/form_add_mission.html'
    form_class = MissionAddForm
    success_url = reverse_lazy('contacts_home')

    def form_valid(self, form):

        form.add_mission(self.request.user)

        return super().form_valid(form)
    
    def form_invalid(self, form):

        print(form)

        return super().form_invalid(form)


class ContactsDeleteMissionFormView(FormView):
    template_name = 'contacts/form_delete_mission.html'
    form_class = MissionDeleteForm
    success_url = reverse_lazy('contacts_home')

    def form_valid(self, form):

        form.delete_mission(self.request.user)

        return super().form_valid(form)
