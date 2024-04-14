from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from main.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "phone", "age", "gender",  "city", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        return user


class UserForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "phone", "age", "gender",  "city"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
