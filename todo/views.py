from django.shortcuts import render, redirect
from todo.models import Task


# Create your views here.
def add_task(request):
    if request.method == "POST":
        data = request.POST
        task = Task.objects.create(
            task=data["task"],
        )

    return redirect("home")
