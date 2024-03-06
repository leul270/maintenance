from django.shortcuts import render

# Create your views here.

def admin_home(request):
    template_name = "admin/home.html"
    return render(request, template_name)
