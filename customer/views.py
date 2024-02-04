from django.shortcuts import render,redirect
from forms import *
# Create your views here.
def create_form(request):
    form = UserForm()
    
    if form.is_valid():
        form = form.save()
        return redirect("user_home")
    context = {"form": form}
    return render(request, "form.html", context)
