from django.db import models
from base.models import *
# from django.contrib.auth.models import AbstractUser

class UserForm(models.Model):
    form_name = models.CharField(
                                max_length=50,)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    administrator = models.ForeignKey(
        Administrator, on_delete=models.CASCADE, default=1)
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE, null=True)

    type_of_network_problem = [
        ("hardware", "Hardware"),
        ("software", "Software"),
    ]

    device_problem = models.CharField(max_length=20, choices=type_of_network_problem)
    short_description = models.TextField(null=True)
    
    fixed =  models.BooleanField(default = False,null=True)
    reviewed =  models.BooleanField(default = False, null=True)



    def __str__(self):
        return self.form_name


class Maintenance(models.Model):
    form_name = models.CharField(
                                max_length=50,)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE, null=True)

    type_of_network_problem = [
        ("computer", "Computer"),
        ("printer", "Printer"),
        ("scanner", "Scanner"),
        ("photo_copy", "Photo Copy"),
        ("others", "Others")
    ]

    device_problem = models.CharField(max_length=20, choices=type_of_network_problem)
    short_description = models.TextField(null=True)
    is_goverment =  models.BooleanField(default = True, null=True)
    fixed =  models.BooleanField(default = False,null=True)
    reviewed =  models.BooleanField(default = False, null=True)



    def __str__(self):
        return self.form_name
class Network(models.Model):
    form_name = models.CharField(
                                max_length=50,)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE, null=True)

    type_of_network_problems = [
        ("slow_internet_connection", "Slow Internet Connection"),
        ("network_connectivity_issues", "Network Connectivity Issues"),
        ("wi_fi_connection_problems", "Wi-Fi Connection Problems"),
        ("network_outage", "Network Outage"),
        ("others", "Others")
    ]

    type_of_network_problem = models.CharField(max_length=100, choices=type_of_network_problems)
    rebooted_modem_router = models.BooleanField(default=False)
    checked_network_cables = models.BooleanField(default=False)
    restarted_computer_device = models.BooleanField(default=False)
    reset_network_settings = models.BooleanField(default=False)
    short_description = models.TextField(null=True)
    aditional_comment = models.TextField(null=True)
    is_goverment =  models.BooleanField(default = True, null=True)
    fixed =  models.BooleanField(default = False,null=True)
    reviewed =  models.BooleanField(default = False, null=True)



    def __str__(self):
        return self.form_name

class Software(models.Model):
    form_name = models.CharField(max_length=50,)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE, null=True)
    software_name = models.CharField(max_length=50,)
    version = models.CharField(max_length=50,)
    operating_system = models.CharField(max_length=50,)

    installation_setup = models.BooleanField(default=False)
    performance_speed = models.BooleanField(default=False)
    functionality_bugs = models.BooleanField(default=False)
    compatibility_integration = models.BooleanField(default=False)
    security_vulnerability = models.BooleanField(default=False)

    short_description = models.TextField(null=True)
    aditional_comment = models.TextField(null=True)

    fixed =  models.BooleanField(default = False,null=True)
    reviewed =  models.BooleanField(default = False, null=True)



    def __str__(self):
        return self.form_name

