from django.contrib.auth import login
from django.views.generic import View
from .forms import LoginForm
from django.shortcuts import render, redirect, reverse
from account_module.models import CustomUser


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data.get('email')
            password = login_form.cleaned_data.get('password')
            user: CustomUser = CustomUser.objects.filter(email__iexact=email).first()
            if user is None:
                login_form.add_error('email', 'نام کاربری یا کلمه عبور اشتباه است')
            elif not user.is_active:
                login_form.add_error('email', 'حساب شما فعال نشده است، ایمیل خود را بررسی کنید.')
            elif not user.check_password(password):
                login_form.add_error('email', 'نام کاربری یا کلمه عبور اشتباه است')
            else:
                login(request, user)
                return redirect('home')
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)
