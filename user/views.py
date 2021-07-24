"""Module user.views"""
from django.views.generic import TemplateView


class UserView(TemplateView):
    """User view"""

    template_name = "user/user.html"
