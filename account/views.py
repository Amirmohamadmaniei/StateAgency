from django.contrib.auth import login, logout
from django.views.generic import FormView, RedirectView, TemplateView, UpdateView
from . import forms
from .forms import CustomUserEditForm
from .models import CustomUser
from .mixins import LoginMixin


class LoginView(LoginMixin, FormView):
    template_name = 'account/login.html'
    form_class = forms.LoginForm
    success_url = '/'

    def form_valid(self, form):
        user = CustomUser.objects.get(phone=form.cleaned_data.get('phone'))
        login(self.request, user)
        return super(LoginView, self).form_valid(form)


class RegisterView(LoginMixin, FormView):
    template_name = 'account/register.html'
    form_class = forms.Register
    success_url = '/'

    def form_valid(self, form):
        user = CustomUser.objects.create_user(phone=form.cleaned_data.get('phone'),
                                              password=form.cleaned_data.get('password'))
        login(self.request, user)
        return super(RegisterView, self).form_valid(form)


class LogoutRedirectView(RedirectView):
    url = '/'

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super().get_redirect_url(*args, **kwargs)


class EditProfileView(UpdateView):
    template_name = 'account/profile_edit.html'
    model = CustomUser
    form_class = CustomUserEditForm
    success_url = '/'
