from django.urls import path
from . import views

urlpatterns = [
    path("", views.todo, name="todos"),
    path("add-todo/", views.add_todo, name="add-todos"),
    path("<slug:slug>/", views.todo_detail, name="todo-detail"),
    path("<slug:slug>/delete-todo/", views.delete_todo, name="todo-delete"),
    path("<slug:slug>/update-todo/", views.update_todo, name="todo-update")
]