from django.contrib import admin
from .models import Staff

# Register your models here.

class StaffAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'designation')
admin.site.register(Staff, StaffAdmin)