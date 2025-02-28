from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Staff(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     designation = models.CharField(max_length=100)
#     type = models.TextChoices("Permanent", "Contract")
#     department = models.CharField(max_length=100)