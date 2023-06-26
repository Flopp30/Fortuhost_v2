from django import forms

from hosted_app.models import HostedApp
from utils.mixins import UserInitiatedFormMixin


class HostedAppForm(UserInitiatedFormMixin, forms.ModelForm):
    class Meta:
        model = HostedApp
        fields = {
            "title",
            "description",
            "status",
        }
