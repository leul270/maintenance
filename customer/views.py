from django.shortcuts import render,redirect
from base.forms import *
from .models import *
from django.views.decorators.csrf import csrf_protect

def customer_home(request):
    context = {}
    return render(request, "user/customer_home.html", context)

def maintenance(request):
    context = {}
    return render(request, "user/maintenance.html", context)
@csrf_protect
def maintenance_form(request):
    form =  Maintenance()
    customer = Customer.objects.get(user_id=2)  #request.user
    if request.method == 'POST':
        form.form_name = request.POST['form_name']
        form.customer = customer
        form.short_description = request.POST['short_description']
        form.device_problem = request.POST['device_problem']

        form.save()
        return redirect('maintenance')
    return render(request, "user/maintenance_form.html")
def network(request):
    context = {}
    return render(request, "user/network.html", context)

@csrf_protect
def network_form(request):
    form =  Network()
    customer = Customer.objects.get(user_id=2)  #request.user
    if request.method == 'POST':
        form.form_name = request.POST['form_name']
        form.customer = customer
        form.type_of_network_problem = request.POST['type_of_network_problem']
        if request.POST.get('troubleshooting_steps'):
            form.rebooted_modem_router= request.POST.get('troubleshooting_steps')
            form.checked_network_cables=request.POST.get('troubleshooting_steps')
            form.restarted_computer_device=request.POST.get('troubleshooting_steps')
            form.reset_network_settings=request.POST.get('troubleshooting_steps')
            
        form.short_description = request.POST['short_description']
        form.aditional_comment = request.POST['aditional_comment']

        form.save()
        return redirect('network')

    context = {}
    return render(request, "user/network_form.html", context)
def software(request):
    context = {}
    return render(request, "user/software.html", context)
def software_form(request):
    context = {}
    return render(request, "user/software_form.html", context)