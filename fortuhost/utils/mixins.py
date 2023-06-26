from typing import Dict, Any

from user.models import User


class NextPageMixin:
    @property
    def success_url(self):
        return self.request.GET.get('next') or self.request.path


class UserInitiatedViewMixin:

    def get_form_kwargs(self) -> Dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class UserInitiatedFormMixin:
    def __init__(self, *args, **kwargs):
        self.user: User = kwargs.pop('user')
        super().__init__(*args, **kwargs)
