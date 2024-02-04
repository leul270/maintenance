from django.shortcuts import render,redirect
from base.models import  Technician
from customer.models import UserForm


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
def fixed(request,pk):
    task = UserForm.objects.get(id=pk)
    task.fixed = True
    task.save()
    return redirect('allTasks')



