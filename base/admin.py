from django.contrib import admin

# Register your models here.
from .models import Customer, Technician, Administrator,  User

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Technician)
admin.site.register(Administrator)

