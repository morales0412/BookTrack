from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomerUserCreationForm, CustomerAuthenticationForm
from django.contrib.auth import login
# Create your views here.


class RegisterView(CreateView):
    form_class = CustomerUserCreationForm
    template_name = "registration/register.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class LoginView(LoginView):
    form_class = CustomerAuthenticationForm
    template_name = "registration/login.html"


class LogoutView(LogoutView):
    pass
