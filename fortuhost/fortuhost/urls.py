from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path(
        "",
        TemplateView.as_view(
            template_name="index.html",
            extra_context={
                "LOGIN_REDIRECT_URL": settings.LOGIN_REDIRECT_URL,
            }
        ),
        name="index",
    ),
    path("admin/", admin.site.urls),
    path("user/", include("user.urls", namespace="user")),
    path("user/", include("hosted_app.urls", namespace="hosted_app")),
    path('auth/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))

urlpatterns += staticfiles_urlpatterns()
