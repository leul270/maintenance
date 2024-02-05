from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "class": "input input--text",
                "placeholder": "Enter your username...",
                "id": "formInput#text",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "input input--password",
                "placeholder": "••••••••",
                "id": "formInput#password",
            }
        )
    )


class CustomerResgistrationForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input input--text",
                "placeholder": "Enter your First name...",
                "id": "formInput#first_name",
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input input--text",
                "placeholder": "Enter your Last name...",
                "id": "formInput#last_name",
            }
        )
    )
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "class": "input input--text",
                "placeholder": "Enter your username...",
                "id": "formInput#username",
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "input input--email",
                "placeholder": "Enter your username...",
                "id": "formInput#email",
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "input input--password",
                "placeholder": "••••••••",
                "id": "formInput#password1",
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "input input--password",
                "placeholder": "••••••••",
                "id": "formInput#password2",
            }
        )
    )

    campus = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input input--text",
                "placeholder": "Enter your Campus...",
                "id": "formInput#campus",
            }
        )
    )
    department = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input input--text",
                "placeholder": "Enter your Department...",
                "id": "formInput#department",
            }
        )
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
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input input--text",
                "placeholder": "Enter your First name...",
                "id": "formInput#first_name",
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input input--text",
                "placeholder": "Enter your Last name...",
                "id": "formInput#last_name",
            }
        )
    )
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "class": "input input--text",
                "placeholder": "Enter your username...",
                "id": "formInput#username",
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "input input--email",
                "placeholder": "Enter your username...",
                "id": "formInput#email",
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "input input--password",
                "placeholder": "••••••••",
                "id": "formInput#password1",
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "input input--password",
                "placeholder": "••••••••",
                "id": "formInput#password2",
            }
        )
    )

    campus = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input input--text",
                "placeholder": "Enter your Campus...",
                "id": "formInput#campus",
            }
        )
    )
    department = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input input--text",
                "placeholder": "Enter your Department...",
                "id": "formInput#department",
            }
        )
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
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input input--text",
                "placeholder": "Enter your First name...",
                "id": "formInput#first_name",
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input input--text",
                "placeholder": "Enter your Last name...",
                "id": "formInput#last_name",
            }
        )
    )
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "class": "input input--text",
                "placeholder": "Enter your username...",
                "id": "formInput#username",
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "input input--email",
                "placeholder": "Enter your username...",
                "id": "formInput#email",
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "input input--password",
                "placeholder": "••••••••",
                "id": "formInput#password1",
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "input input--password",
                "placeholder": "••••••••",
                "id": "formInput#password2",
            }
        )
    )

    campus = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input input--text",
                "placeholder": "Enter your Campus...",
                "id": "formInput#campus",
            }
        )
    )
    department = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input input--text",
                "placeholder": "Enter your Department...",
                "id": "formInput#department",
            }
        )
    )

    work_experiance = forms.IntegerField( 
        widget=forms.NumberInput(
            attrs={
                "class": "input input--text",
                "placeholder": "Enter your Department...",
                "id": "formInput#experiance",
            }
        ))
    SKILL_LEVEL_CHOICES = (
        (1, "Beginner"),
        (2, "Intermediate"),
        (3, "Advanced"),
    )
    skill_level = forms.ChoiceField(choices=SKILL_LEVEL_CHOICES,   
        widget=forms.Select(
            attrs={
                "class": "uk-select",
                "aria-label":"Select",
                "placeholder": "",
                "id": "formInput#level",
            }
        ))
    short_description = forms.CharField(    
        widget=forms.Textarea(
            attrs={
                "class": "input input--select",
                "placeholder": "Description...",
                "id": "formInput#description",
                
            }
        ))

    administrator = forms.ModelChoiceField(
        queryset=Administrator.objects.all(), required=False,
         widget=forms.Select(
            attrs={
                "class": "input input--text",
                "placeholder": "",
                "id": "formInput#admin",
            }
        )
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
        ]

    def save(self, commit=True):
        user = super().save()
        department = self.cleaned_data["department"]
        work_experiance = self.cleaned_data["work_experiance"]
        campus = self.cleaned_data["campus"]
        skill_level = self.cleaned_data["skill_level"]
        administrator = self.cleaned_data["administrator"]
        technician = Technician.objects.create(
            user=user,
            department=department,
            campus=campus,
            work_experiance=work_experiance,
            skill_level=skill_level,
            administrator=administrator,
        )
        technician.is_technician = True
        technician = technician.save()
        return technician
