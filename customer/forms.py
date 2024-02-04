
from django import forms
from django.forms import ModelForm
from .models import *


class UserForm(ModelForm):
    class Meta:
        model = UserForm
        fields = "__all__"

