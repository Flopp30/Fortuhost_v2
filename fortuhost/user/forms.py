from django import forms

from hosted_app.models import HostedApp


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = HostedApp
        fields = {
            "password1",
            "password2",
            "email",
        }
        widgets = {
            "password1": forms.PasswordInput,
            "password2": forms.PasswordInput,
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = HostedApp
        fields = {
            "password1",
            "email",
        }
        widgets = {
            "password1": forms.PasswordInput,
        }
