from django.shortcuts import render, get_object_or_404, redirect
from django.utils.dateparse import parse_datetime
from .models import Todos

# Create your views here.


def todo(request):
    Todos_incomplete = Todos.objects.filter(is_complete=False).order_by("due_date")
    Todos_complete = Todos.objects.filter(is_complete=True).order_by("-due_date")
    return render(request, "todos/todos.html",
        {"todos_incomplete": Todos_incomplete, "todos_completed": Todos_complete},
    )


def add_todo(request):
    if request.method == "POST":
        title_value = request.POST.get("title")
        description_value = request.POST.get("description")
        due_date_value = request.POST.get("due-date") or None

        Todos.objects.create(
            title=title_value,
            description=description_value,
            due_date=due_date_value,
        )
        return redirect("todos")
    return render(request, "todos/add-todo.html")


def todo_detail(request, slug):
    todo = get_object_or_404(Todos, todo_slug=slug)
    return render(request, "todos/todo-detail.html", {
        "todo": todo,
        "title": todo.title,
        "description": todo.description,
        "created_at": todo.created_at,
        "due_date": todo.due_date,
        "is_complete": todo.is_complete,
    })


def delete_todo(request, slug):
    todo = get_object_or_404(Todos, todo_slug=slug)
    if request.method == "POST":
        todo.delete()
        return redirect("todos")
    return redirect("todo-detail", slug=slug)


def update_todo(request, slug):
    todo = get_object_or_404(Todos, todo_slug=slug)
    if request.method == "POST":
        todo.title = request.POST.get("title", "").strip() or todo.title
        todo.description = request.POST.get("description", "").strip() or todo.description
        due_date_value = request.POST.get("due-date") or None
        todo.due_date = parse_datetime(due_date_value) if due_date_value else None
        todo.is_complete = request.POST.get("is-complete") == "on"
        todo.save()
        return redirect("todo-detail", slug=todo.todo_slug)
    return render(request, "todos/update-todo.html", {
        "todo": todo,
        "title": todo.title,
        "description": todo.description or "",
        "due_date": todo.due_date,
        "is_complete": todo.is_complete,
    })
