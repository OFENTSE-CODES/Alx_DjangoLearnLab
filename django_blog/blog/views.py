from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User

# Registration
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form": form})


# Profile view + edit
@login_required
def profile(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if email:
            request.user.email = email
            request.user.save()
            return redirect("profile")
    return render(request, "registration/profile.html")