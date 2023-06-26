from django.urls import path

from sign.views import SigninView, SignupView, SignoutView

app_name = "sign"
urlpatterns = [
    path(
        "signup/",
        SignupView.as_view(),
        name="signup",
    ),
    path(
        "signin/",
        SigninView.as_view(),
        name="signin",
    ),
    path(
        "signout/",
        SignoutView.as_view(),
        name="signout",
    ),
]
