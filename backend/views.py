from django.shortcuts import render
from todo.models import Task


def home(request):
    pending_tasks = Task.objects.filter(is_completed=False)

    completed_tasks = Task.objects.filter(is_completed=True)

    context = {
        "pending_tasks": pending_tasks,
        "completed_tasks": completed_tasks,
    }

    return render(request, "home-todo.html", context=context)
