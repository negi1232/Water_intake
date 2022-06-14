from django.shortcuts import render

# ここから追加
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
#from .forms import LoginForm
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired, loads, dumps
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, resolve_url
from django.template.loader import render_to_string
from django.views import generic
from .forms import (
    LoginForm, UserCreateForm, UserUpdateForm,
)

User = get_user_model()

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'login.html'
# ここまで追加

class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser


class UserDetail(OnlyYouMixin, generic.DetailView):
    model = User
    template_name = 'user_detail.html'
            

class UserUpdate(OnlyYouMixin, generic.UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'user_form.html'

    def get_success_url(self):
        return resolve_url('accounts:user_detail', pk=self.kwargs['pk'])

from django.views.generic import FormView

