from django.shortcuts import render, redirect
from django.urls import path
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_customer:
                    dashboard_redirect = 'customer_home'
                elif user.is_technician:
                    dashboard_redirect = 'tech_home'
                elif user.is_staff:
                    dashboard_redirect = 'admin:index'
                else:
                    # Handle other user types if needed
                    messages.error(request, 'Invalid user type')
                    return redirect('login')
                
                login(request, user)
                return redirect(dashboard_redirect)
            else:
                messages.error(request, 'Invalid login credentials')
                return redirect('login')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def customer_registration(request):
    template_name = "user/registration.html"

    if request.method == "POST":
        form = CustomerResgistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomerResgistrationForm()

    return render(request, template_name, {"form": form})

def signup_selection(request):
    template_name = "signup_selection.html"
    return render(request, template_name)



def technician_registration(request):
    template_name = "technician/registration.html"

    if request.method == "POST":
        form = TechnicianResgistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login") # Replace 'home' with the actual URL you want to redirect to after registration
    else:
        form = TechnicianResgistrationForm()

    return render(request, template_name, {"form": form})


def administrator_registration(request):
    template_name = "administrator/registration.html"

    if request.method == "POST":
        form = AdministratorResgistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login")
    else:
        form = AdministratorResgistrationForm()

    return render(request, template_name, {"form": form})


@login_required(login_url="/login/")
def home(request):
    context = {}
    return render(request, "home.html", context)


def user_home(request, id):
    USERFORM = user_form.objects.get(id=id)
    context = {"USERFORM": USERFORM}
    return render(request, "user/user_home.html", context)


def technician_home(request, id):
    context = {}
    return render(request, "technician/technician_home.html", context)


def administrator_home(request, id):
    USERFORM = user_form.objects.select_related("customer").all()
    USERFORM = user_form.objects.filter(customer__isnull=False)
    # USERFORM=user_form.objects.all()
    context = {"USERFORM": USERFORM}
    return render(request, "administrator/administrator_home.html", context)




# def device_create(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             device = form.save()
#             # Process the form data and redirect
#     else:
#         form = UserForm()
#         hardware_form = HardwareForm()
#         software_form = SoftwareForm()

#     return render(request, 'device_create.html', {
#         'form': form,
#         'hardwareForm': hardware_form,
#         'softwareForm': software_form
#     })
