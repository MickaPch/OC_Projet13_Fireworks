from django import forms
from accounts.models import User


class EditUsername(forms.ModelForm):

    user_pk = forms.IntegerField()

    class Meta:
        model = User
        fields = [
            'username'
        ]

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control form-element user-input user-username-input'
                }
            )
        }

    def edit_username(self):
        user_pk = self.cleaned_data['user_pk']
        user = User.objects.get(pk=user_pk)

        user.username = self.cleaned_data['username']

        user.save()

class EditName(forms.ModelForm):

    user_pk = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super(EditName, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
        ]

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control form-element user-input user-first_name-input',
                    'placeholder': 'First name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control form-element user-input user-last_name-input',
                    'placeholder': 'Last name'
                }
            )
        }

    def edit_name(self):
        user_pk = self.cleaned_data['user_pk']
        user = User.objects.get(pk=user_pk)

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        user.save()


class EditEmail(forms.ModelForm):

    user_pk = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super(EditEmail, self).__init__(*args, **kwargs)
        self.fields['email'].required = False

    class Meta:
        model = User
        fields = [
            'email'
        ]

        widgets = {
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control form-element user-input user-email-input',
                    'placeholder': 'First name'
                }
            )
        }

    def edit_email(self):
        user_pk = self.cleaned_data['user_pk']
        user = User.objects.get(pk=user_pk)

        user.email = self.cleaned_data['email']

        user.save()
