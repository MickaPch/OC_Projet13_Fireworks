"""Module user.views"""
from django.views.generic import TemplateView


class ContactsHomeView(TemplateView):
    """Contacts Home view"""

    template_name = "contacts/contacts.html"
