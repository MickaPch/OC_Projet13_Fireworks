"""Module user.views"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class ContactsHomeView(LoginRequiredMixin, TemplateView):
    """Contacts Home view"""

    template_name = "contacts/contacts.html"
