from django import forms
from django.contrib.auth.forms import UserCreationForm

from shop.models import UserModel


class UserForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("username",)
