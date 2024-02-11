
from django import forms
from django.forms import ModelForm
from .models import *


class UserForm(ModelForm):
    class Meta:
        model = UserForm
        fields = "__all__"

    #  def save(self, commit=True):

    #     reset_network_settings = self.cleaned_data["reset_network_settings"]
    #     userform = UserForm.objects.create(
    #         user=user, department=department, campus=campus
    #     )
    #     customer = customer.save()
    #     return user

