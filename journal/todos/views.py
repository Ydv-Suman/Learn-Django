from django.shortcuts import render, get_object_or_404
from .models import Todos

# Create your views here.


def todo(request):
    Todos_incomplete = Todos.objects.filter(is_complete=False).order_by("due_date")
    Todos_complete = Todos.objects.filter(is_complete=True).order_by("-due_date")
    return render(request, "todos/todos.html",
        {"todos_incomplete": Todos_incomplete, "todos_completed": Todos_complete},
    )

def todo_detail(request, slug):
    todo = get_object_or_404(Todos, todo_slug=slug)
    return render(request, "todos/todo-detail.html", {
        "title": todo.title,
        "description": todo.description,
        "created_at": todo.created_at,
        "due_date": todo.due_date,
        "is_complete": todo.is_complete,
    })