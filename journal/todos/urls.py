from django.urls import path
from . import views

urlpatterns = [
    path("", views.todo, name="todos"),
    path("<slug:slug>/", views.todo_detail, name="todo-detail")
]