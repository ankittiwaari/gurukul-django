from django.db import models
from django.contrib.auth.models import User
from departments.models import Department

# Create your models here.
class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    type = models.TextChoices("Permanent", "Contract")
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['user__username']
        verbose_name_plural = 'Staff members'