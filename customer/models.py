from django.db import models
from base.models import *
# from django.contrib.auth.models import AbstractUser

class UserForm(models.Model):
    form_name = models.CharField(
                                max_length=50,)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    administrator = models.ForeignKey(
        Administrator, on_delete=models.CASCADE, default=1
    )
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE, null=True)

    DEVICE_PROBLEM_CHOICES = [
        ("hardware", "Hardware"),
        ("software", "Software"),
    ]

    device_problem = models.CharField(max_length=20, choices=DEVICE_PROBLEM_CHOICES)
    short_description = models.TextField(null=True)
    
    fixed =  models.BooleanField(default = False,null=True)
    reviewed =  models.BooleanField(default = False, null=True)



#     def __str__(self):
#         return self.form_name


