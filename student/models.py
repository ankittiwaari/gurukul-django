from django.contrib.auth.models import User
from django.db import models
from standards.models import Standard

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,  limit_choices_to={"is_staff": False})
    standard = models.ForeignKey(Standard, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        ordering = ['user__first_name', 'user__last_name']
        verbose_name_plural = 'Students'