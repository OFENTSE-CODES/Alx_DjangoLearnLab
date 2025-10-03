from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm


class CustomLoginView(LoginView):
    template_name = 'blog/login.html'


class CustomLogoutView(LogoutView):
    template_name = 'blog/logout.html'


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('blog:profile')
    else:
        form = SignUpForm()
    return render(request, 'blog/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('blog:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'blog/profile.html', {'u_form': u_form, 'p_form': p_form})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProfileForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.models import User

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log the user in immediately after registration
            messages.success(request, "Registration successful. You are now logged in.")
            return redirect("home")
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form": form})

@login_required
def profile_view(request):
    # Show profile; also handle edits
    if request.method == "POST":
        uform = UserUpdateForm(request.POST, instance=request.user)
        pform = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            messages.success(request, "Your profile has been updated.")
            return redirect("profile")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        uform = UserUpdateForm(instance=request.user)
        pform = ProfileForm(instance=request.user.profile)
    return render(request, "registration/profile.html", {"uform": uform, "pform": pform})