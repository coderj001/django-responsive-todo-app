from django.contrib import admin
from .models import ToDoList
# Register your models here.

class AdminView(admin.ModelAdmin):
    list_display=('item', 'status')

admin.site.register(ToDoList, AdminView)