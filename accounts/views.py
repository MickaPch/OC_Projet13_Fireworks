"""Module user.views"""
from django.views.generic import TemplateView


class AccountsHomeView(TemplateView):
    """AccountsHome view"""

    template_name = "accounts/home.html"
