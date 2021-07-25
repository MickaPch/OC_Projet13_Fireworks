"""Module user.views"""
from django.views.generic import TemplateView


class AccountsHomeView(TemplateView):
    """Accounts Home view"""

    template_name = "accounts/accounts.html"

class AccountsProfileView(TemplateView):
    """Accounts Profile view"""

    template_name = "accounts/profile.html"
