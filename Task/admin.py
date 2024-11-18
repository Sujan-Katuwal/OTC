from django.contrib import admin
from .models import Task

# Register your models here.
admin.site.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'due_date')
    list_filter = ('status', 'due_date')
