from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from .models import User
from .forms import RegistrationForm


# Create your views here.
class UserLoginView(LoginView):
    template_name = 'usersapp/login.html'


class UserCreateView(CreateView):
    model = User
    template_name = 'usersapp/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('usersapp:login')
