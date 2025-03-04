from django.db import models
from staff.models import Staff
from subjects.models import Subject

# Create your models here.
class Standard(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=15)
    class_teacher = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    subjects = models.ManyToManyField(Subject)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title