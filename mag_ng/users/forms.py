from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
   
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email','first_name','last_name','avatar','bio','social_handle',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email','first_name','last_name','avatar','bio','social_handle',)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_guest = True
        user.save
        return user
