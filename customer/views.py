from django.shortcuts import render,redirect
from base.forms import *
from .models import *
# Create your views here.
# def create_form(request):
#     form = UserForm()
    
#     if form.is_valid():
#         form = form.save()
#         return redirect("user_home")
#     context = {"form": form}
#     return render(request, "form.html", context)

def customer_home(request):
    context = {}
    return render(request, "user/customer_home.html", context)

def maintenance(request):
    context = {}
    return render(request, "user/maintenance.html", context)
def maintenance_form(request):
    form =  Maintenance()
    customer = Customer.objects.get(user_id=2)  #request.user
    if request.method == 'POST':
        form.form_name = request.POST['form_name']
        form.customer = customer
        form.short_description = request.POST['short_description']
        form.short_description = request.POST['device_problem']
        form.save()
        return redirect('customer_home')
       


            
    

    return render(request, "user/maintenance_form.html")
def network(request):
    context = {}
    return render(request, "user/network.html", context)
def network_form(request):
    context = {}
    return render(request, "user/network_form.html", context)
def software(request):
    context = {}
    return render(request, "user/software.html", context)
def software_form(request):
    context = {}
    return render(request, "user/software_form.html", context)
# def customer_registration(request):
    customer=customer.objects.all()
    if request.method == 'POST':
        
        first_name=request.POST['user.first_name']
        last_name=request.POST['user.last_name']
        department=request.POST['department']
        campus=request.POST['campus']
        email=request.POST['email']
        password=request.POST['password1']
        confirm_password=request.POST['password2']

        new_customer =customer(first_name=first_name,last_name=last_name,department=department,
                                                campus=campus,email=email,password=password,confirm_password=password)
        new_customer.save()
        return redirect('customer_home')
    
    context = {'customer' :customer}
    return render(request, "user/customer_home.html", context)