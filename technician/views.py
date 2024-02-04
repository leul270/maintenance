from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'technician/home.html')

def detail(request,pk):
    return render(request, 'technician/detail.html')

def updateProfile(request,pk):
    return render(request, 'technician/updateProfile.html')
def allTasks(request):
    return render(request, 'technician/allTasks.html')


