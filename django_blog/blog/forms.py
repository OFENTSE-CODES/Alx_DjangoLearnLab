from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Profile
        fields = ("bio", "avatar")

    def __init__(self, *args, **kwargs):
        # Expect the user instance to be passed in kwargs as 'user'
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.initial["email"] = self.user.email

    def save(self, commit=True):
        profile = super().save(commit=False)
        # update user email
        if self.user:
            self.user.email = self.cleaned_data.get("email", self.user.email)
            if commit:
                self.user.save()
        if commit:
            profile.save()
        return profile