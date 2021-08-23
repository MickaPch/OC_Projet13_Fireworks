"""Module user.views"""
from accounts.models import User
from django.http.response import JsonResponse
from accounts.forms import EditUsername, EditName, EditEmail
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


class AccountsHomeView(TemplateView):
    """Accounts Home view"""

    template_name = "accounts/accounts.html"

class AccountsProfileView(TemplateView):
    """Accounts Profile view"""

    template_name = "accounts/profile.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['form_username'] = self.get_form_username()
        context['form_name'] = self.get_form_name()
        context['form_email'] = self.get_form_email()

        return context

    def get_form_username(self):

        data = {
            'user_pk': self.request.user.pk,
            'username': self.request.user.username
        }
        form = EditUsername(data=data)
        return form

    def get_form_name(self):

        data = {
            'user_pk': self.request.user.pk,
            'first_name': self.request.user.first_name,
            'last_name': self.request.user.last_name
        }
        form = EditName(data=data)
        return form

    def get_form_email(self):

        data = {
            'user_pk': self.request.user.pk,
            'email': self.request.user.email
        }
        form = EditEmail(data=data)
        return form


@login_required
def edit_username(request):

    form = EditUsername(request.POST)

    if form.is_valid():
        form.edit_username()
    else:
        print(form)

    return JsonResponse({
        'username': form.cleaned_data['username']
    })

@login_required
def edit_name(request):

    form = EditName(request.POST)

    if form.is_valid():
        form.edit_name()
    else:
        print(form)

    return JsonResponse({
        'first_name': form.cleaned_data['first_name'],
        'last_name': form.cleaned_data['last_name']
    })

@login_required
def edit_email(request):

    form = EditEmail(request.POST)

    if form.is_valid():
        form.edit_email()
    else:
        print(form)

    return JsonResponse({
        'email': form.cleaned_data['email']
    })
