from django import forms

from hosted_app.models import HostedApp


class AppForm(forms.ModelForm):
    class Meta:
        model = HostedApp
        fields = {
            "title",
            "description",
            "status",
        }
        widgets = {
            "status": forms.ChoiceField,
        }
