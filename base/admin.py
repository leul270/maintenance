from django.contrib import admin

# Register your models here.
from .models import Customer, Technician, Administrator,  User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username","is_active"]
    list_editable = ["is_active"]
    ordering = ["is_active"]
    # list_per_page = 10
    search_fields = ["username__istartswith"]





admin.site.register(Customer)
admin.site.register(Technician)
admin.site.register(Administrator)

