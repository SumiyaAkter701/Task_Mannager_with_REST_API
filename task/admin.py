from django.contrib import admin
from .models import Task,Task_Image
# Register your models here.
class Task_Display(admin.ModelAdmin):
    list_display=['title','priority','created_date','due_date','updated_date','is_complete']
    list_filter=['priority','created_date','due_date','is_complete']
    search_fields=['title']

admin.site.register(Task,Task_Display)
admin.site.register(Task_Image)