from django.shortcuts import render,redirect
from base.models import  Technician
from customer.models import Maintenance,Network,Software
from .models import TechnicianForm
from itertools import chain

def home(request):
    technician = request.user.id
    maintenance_tasks = Maintenance.objects.filter(technician=technician)
    network_tasks = Network.objects.filter(technician=technician)
    software_tasks = Software.objects.filter(technician=technician)
    context = {'maintenance_tasks':maintenance_tasks,'network_tasks':network_tasks,'software_tasks':software_tasks}

    return render(request, 'technician/home.html', context)

def detail(request,pk, parameter):
    if parameter == "maintenance":
        single_task = Maintenance.objects.get(id=pk)
        context = {'single_task':single_task}
    elif parameter == "network":
        single_task = Network.objects.get(id=pk)
        context = {'single_task':single_task}
    else:
        software_tasks = Software.objects.get(id=pk)
        context = {'software_tasks':software_tasks}
    
    
    return render(request, 'technician/detail.html',context)

def networkDetail(request,pk):
    single_task = Network.objects.get(id=pk)
    context = {'single_task':single_task}
    return render(request, 'technician/networkDetial.html',context)
def updateProfile(request,pk):
    return render(request, 'technician/updateProfile.html')
def maintenanceTasks(request):
    technician = request.user.id
    maintenance_tasks = Maintenance.objects.filter(technician=technician)
    context = {'maintenance_tasks':maintenance_tasks}
    return render(request, 'technician/maintenance.html',context)

def networkTaks(request):
    technician = request.user.id
    network_tasks = Network.objects.filter(technician=technician)
    context = {'network_tasks':network_tasks}
    return render(request, 'technician/network.html',context)

def softwareTaks(request):
    technician = request.user.id
    software_tasks = Software.objects.filter(technician=technician)
    context = {'software_tasks':software_tasks}
    return render(request, 'technician/software.html',context)

def isFixed(request,pk):
    technicianForm  = TechnicianForm()
    task = UserForm.objects.get(id=pk)
    if request.method == 'POST':
        is_fixed = request.POST['is_fixed']
        if is_fixed =="True":
            task.fixed = True
            task.save()
            technicianForm.task = task
            technicianForm.short_description= request.POST['short_description']
            technicianForm.is_fixed = True
            technicianForm.save()
            return redirect('home')
        else:
            technicianForm.task = task
            technicianForm.short_description= request.POST['short_description']
            technicianForm.reason= request.POST['reason']
            technicianForm.solution= request.POST['solution']
            technicianForm.save()

            return redirect('home')
    return redirect('home')



