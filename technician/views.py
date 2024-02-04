from django.shortcuts import render,redirect
from base.models import user_form, Technician


# Create your views here.


def home(request):
    technician = Technician.objects.get(user= 15)
    tasks = user_form.objects.filter(technician=technician)
    context = {'tasks':tasks}

    return render(request, 'technician/home.html', context)

def detail(request,pk):
    single_task = user_form.objects.get(id =pk)
    
    context = {'single_task':single_task}
    return render(request, 'technician/detail.html',context)

def updateProfile(request,pk):
    return render(request, 'technician/updateProfile.html')
def allTasks(request):
    technician = Technician.objects.get(user= 15)
    tasks = user_form.objects.filter(technician=technician)
 
    context = {'tasks':tasks}
    return render(request, 'technician/allTasks.html',context)
def fixed(request,pk):
    task = user_form.objects.get(id=pk)
    task.fixed = True
    task.save()
    return redirect('allTasks')



