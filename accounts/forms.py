from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class CustomerUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class CustomerAuthenticationForm(AuthenticationForm):
    pass
