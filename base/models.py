from random import choice
from django.db import models

# from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_technician = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    department = models.CharField(max_length=100)
    campus = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)
    phone_number = models.IntegerField(null= True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Administrator(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    department = models.CharField(max_length=100)
    campus = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Technician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    department = models.CharField(max_length=100)
    EXPERT_ON_CHOICES = (
        ("Maintenance", "Maintenance"),
        ("Network", "Network"),
        ("Software", "Software"),
        ("Software", "Software"),
    )
    expert_on = models.CharField(max_length=20, choices=EXPERT_ON_CHOICES)
    campus = models.CharField(max_length=50)
    work_experiance = models.IntegerField()
    phone_number = models.IntegerField(null= True)

    SKILL_LEVEL_CHOICES = (
        (1, "Beginner"),
        (2, "Intermediate"),
        (3, "Advanced"),
    )
    skill_level = models.IntegerField(choices=SKILL_LEVEL_CHOICES)
    short_description = models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


