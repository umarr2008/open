from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView, View, CreateView

from .forms import UserSignupForm, UserSigninForm
from .models import User

from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserSignupForm


class UserRegisterView(CreateView):
    model = User
    form_class = UserSignupForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('login')
    context_object_name = 'form'

    def form_valid(self, form):
        user = form.save()
        user.set_password(user.password1)
        user.is_active = True
        user.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserSignupForm()
        return context


class UserLoginView(FormView):
    form_class = UserSigninForm
    template_name = 'auth/login.html'
    success_url = reverse_lazy('home_page')
    context_object_name = 'form'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')

        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            messages.error(self.request, 'Username or password is incorrect')
            return redirect('login')

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserSigninForm()
        return context


class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('dashboard')
