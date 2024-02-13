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
    customer = Customer.objects.get(user_id=5)  #request.user
    if request.method == 'POST':
        # print(request.POST.get("reset_network_settings"))
        form.form_name = request.POST['form_name']
        form.customer = customer
        form.type_of_network_problem = request.POST['type_of_network_problem']


        if request.POST.get('rebooted_modem_router'):
            form.rebooted_modem_router= True
        else:
            form.rebooted_modem_router= False

        if request.POST.get('checked_network_cables'):
            form.checked_network_cables= True
        else:
            form.checked_network_cables= False

        if request.POST.get('restarted_computer_device'):
            form.restarted_computer_device= True
        else:
            form.restarted_computer_device= False

        if request.POST.get('reset_network_settings'):
            form.reset_network_settings= True
        else:
            form.reset_network_settings= False

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
    form =  Software()
    customer = Customer.objects.get(user_id=5)  #request.user
    if request.method == 'POST':
        # print(request.POST.get("reset_network_settings"))
        form.form_name = request.POST['form_name']
        form.customer = customer
        form.software_name = request.POST['software_name']
        form.version = request.POST['version']
        form.operating_system = request.POST['operating_system']

        if request.POST.get('installation_setup'):
            form.installation_setup= True
        else:
            form.installation_setup= False

        if request.POST.get('performance_speed'):
            form.performance_speed= True
        else:
            form.performance_speed= False

        if request.POST.get('functionality_bugs'):
            form.functionality_bugs= True
        else:
            form.functionality_bugs= False

        if request.POST.get('compatibility_integration'):
            form.compatibility_integration= True
        else:
            form.compatibility_integration= False

        if request.POST.get('security_vulnerability'):
            form.security_vulnerability= True
        else:
            form.security_vulnerability= False

        form.short_description = request.POST['short_description']
        form.aditional_comment = request.POST['aditional_comment']

        form.save()
        return redirect('software')
    
    context = {}
    return render(request, "user/software_form.html", context)