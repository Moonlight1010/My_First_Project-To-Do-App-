from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'done')
    list_display_link = ('title',)
    list_filter = ('title',)
    search_fields = ('title', 'description')
