from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from hosted_app.forms import HostedAppForm
from hosted_app.models import HostedApp
from utils.mixins import NextPageMixin, UserInitiatedViewMixin


class HostedAppListView(NextPageMixin, ListView):
    model = HostedApp
    ordering = 'pk'
    template_name = "hosted_app/list.html"

    def get_queryset(self):
        return super().get_queryset().filter(
            user=self.request.user
        )


class HostedAppCreateView(NextPageMixin, UserInitiatedViewMixin, CreateView):
    form_class = HostedAppForm
    model = HostedApp
    success_url = reverse_lazy("hosted_app:list")
    template_name = "hosted_app/create.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)


class HostedAppUpdateView(NextPageMixin, UserInitiatedViewMixin, UpdateView):
    model = HostedApp
    form_class = HostedAppForm
    success_url = reverse_lazy("hosted_app:list")
    template_name = "hosted_app/update.html"
