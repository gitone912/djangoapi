from django.contrib import admin
from .models import student
# Register your models here.
@admin.register(student)
class studentdata(admin.ModelAdmin):
    list_display=['id','name','roll','city']