from django.contrib import admin
from .models import Todos

# Register your models here.

class TodosAdmin(admin.ModelAdmin):
    prepopulated_fields = {"todo_slug": ("title",)}

admin.site.register(Todos, TodosAdmin)