import logging

from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from allauth.account.views import (
    SignupView as _SignupView,
)

from django.conf import settings

logger = logging.getLogger(__name__)


class SigninView(LoginView):
    success_url = settings.LOGIN_REDIRECT_URL
    redirect_authenticated_user = True
    template_name = "sign/signin.html"

    def post(self, request,  *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                logger.info(f'Successful login by user {user}')
                return HttpResponseRedirect(self.get_success_url())
        logger.warning(f'Unsuccessfull login attempt from IP {request.META.get("REMOTE_ADDR")}')
        return self.form_invalid(form)


class SignoutView(LogoutView):
    next_page: str = settings.LOGOUT_REDIRECT_URL


class SignupView(_SignupView):
    success_url: str = settings.LOGIN_REDIRECT_URL
    template_name = "sign/signup.html"
