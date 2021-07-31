"""Module user.views"""
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Home view"""

    template_name = "dashboard/home.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['active_page'] = 'dashboard'

        return context
