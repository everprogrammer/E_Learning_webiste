from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .forms import CustomUserCreationForm
from django.contrib import messages


# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f'You have successfully logged in as {request.user.username}')
                    return redirect('/')
                messages.info(request, f'User does not exist! Please sign up.')
            messages.info(request, f'Username and password does not match')
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'auth/login.html', context)
    return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, f'You have successfully logged out!')
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserCreationForm(data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'You have successfully signed up.')
                return redirect('/')
            else:
                messages.error(request,'OOPS! An Error occurred while signing up!')
            
        form = CustomUserCreationForm()
        context = {'form': form}
        return render(request, 'auth/signup.html', context)
    else:
        return redirect('/')
    

def password_reset_view(request):
    
    return PasswordResetView.as_view(
        email_template_name='auth/password_reset_email.html',
        success_url= reverse('auth_app:password_reset_done'),
        template_name='auth/password_reset.html',
        form_class=PasswordResetForm
    )(request)

def password_reset_done_view(request):
    return PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html')(request)

def password_reset_confirm_view(request, uidb64, token):
    return PasswordResetConfirmView.as_view(
        template_name='auth/password_reset_confirm.html',
        success_url=reverse_lazy('auth_app:password_reset_complete')
    )(request, uidb64=uidb64, token=token)

def password_reset_complete_view(request):
    return PasswordResetCompleteView.as_view(template_name='auth/password_reset_complete.html')(request)
