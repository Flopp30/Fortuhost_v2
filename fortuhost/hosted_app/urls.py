from django.urls import path

from hosted_app.views import HostedAppListView, HostedAppCreateView, HostedAppUpdateView

app_name = "hosted_app"

urlpatterns = [
    path("list/", HostedAppListView.as_view(), name="list"),
    path("create/", HostedAppCreateView.as_view(), name="create"),
    path("update/<int:pk>/", HostedAppUpdateView.as_view(), name="update"),
]
