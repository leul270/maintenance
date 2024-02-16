from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UserForm)
admin.site.register(Maintenance)
admin.site.register(Network)
admin.site.register(Software)