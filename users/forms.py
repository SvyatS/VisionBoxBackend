from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group

from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    groups = forms.ModelChoiceField(queryset=Group.objects.all())
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'avatar', 'full_name', 'phone_number')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'avatar', 'full_name', 'phone_number')