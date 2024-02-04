from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *


class CustomerResgistrationForm(UserCreationForm):
    department = forms.CharField(max_length=50)
    campus = forms.CharField(max_length=50)

    class Meta(UserCreationForm.Meta):
        model = User
        # fields = "__all__"
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
            "department",
            "campus",
        ]

    def save(self, commit=True):
        user = super().save()
        department = self.cleaned_data["department"]
        campus = self.cleaned_data["campus"]
        customer = Customer.objects.create(
            user=user, department=department, campus=campus
        )
        customer.is_customer = True
        customer = customer.save()
        return user


class AdministratorResgistrationForm(UserCreationForm):
    department = forms.CharField(max_length=50)
    campus = forms.CharField(max_length=50)

    class Meta(UserCreationForm.Meta):
        model = User
        # fields = "__all__"
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
            "department",
            "campus",
        ]

    def save(self, commit=True):
        user = super().save()
        department = self.cleaned_data["department"]
        campus = self.cleaned_data["campus"]
        administrator = Administrator.objects.create(
            user=user, department=department, campus=campus
        )
        administrator.is_staff = True
        administrator = administrator.save()
        return user


class TechnicianResgistrationForm(UserCreationForm):
    department = forms.CharField(max_length=50)
    campus = forms.CharField(max_length=50)
    phone_number = forms.IntegerField()

    work_experiance = forms.IntegerField()
    SKILL_LEVEL_CHOICES = (
        (1, "Beginner"),
        (2, "Intermediate"),
        (3, "Advanced"),
    )
    skill_level = forms.ChoiceField(choices=SKILL_LEVEL_CHOICES)
    short_description = forms.CharField(widget=forms.Textarea)

    administrator = forms.ModelChoiceField(
        queryset=Administrator.objects.all(), required=False
    )

    class Meta(UserCreationForm.Meta):
        model = User
        # fields = "__all__"
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
            "department",
            "campus",
            'phone_number'
        ]

    def save(self, commit=True):
        user = super().save()
        department = self.cleaned_data["department"]
        work_experiance = self.cleaned_data["work_experiance"]
        campus = self.cleaned_data["campus"]
        skill_level = self.cleaned_data["skill_level"]
        administrator = self.cleaned_data["administrator"]
        phone_number = self.cleaned_data["phone_number"]
        technician = Technician.objects.create(
            user=user,
            department=department,
            campus=campus,
            work_experiance=work_experiance,
            skill_level=skill_level,
            administrator=administrator,
            phone_number=phone_number,
        )
        technician = technician.save()
        return technician


class UserForm(ModelForm):
    class Meta:
        model = user_form
        fields = "__all__"


class HardwareForm(ModelForm):
    class Meta:
        model = hardware_form
        fields = "__all__"


class SoftwareForm(ModelForm):
    class Meta:
        model = software_form
        fields = "__all__"
