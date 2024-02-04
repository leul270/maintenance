from django.shortcuts import render,redirect
from base.models import  Technician
from customer.models import UserForm
from .models import TechnicianForm


# Create your views here.


def home(request):
    technician = Technician.objects.get(user= 15)
    tasks = UserForm.objects.filter(technician=technician)
    context = {'tasks':tasks}

    return render(request, 'technician/home.html', context)

def detail(request,pk):
    single_task = UserForm.objects.get(id =pk)
    
    context = {'single_task':single_task}
    return render(request, 'technician/detail.html',context)

def updateProfile(request,pk):
    return render(request, 'technician/updateProfile.html')
def allTasks(request):
    technician = Technician.objects.get(user= 15)
    tasks = UserForm.objects.filter(technician=technician)
 
    context = {'tasks':tasks}
    return render(request, 'technician/allTasks.html',context)
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



