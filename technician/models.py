from django.db import models
from customer.models import UserForm

# Create your models here.


class TechnicianForm(models.Model):
    task = models.ForeignKey(UserForm, on_delete=models.CASCADE)
    short_description = models.TextField(null=True)

    is_fixed = models.BooleanField(default=False)
    reason = models.TextField(null=True)
    solution = models.TextField(null=True)
    
    def __str__(self):
        return self.task.form_name
    