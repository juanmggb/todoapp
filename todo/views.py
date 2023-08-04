from django.shortcuts import get_object_or_404, redirect, render
from todo.models import Task
from todo.forms import TaskForm


# Create your views here.
def add_task(request):
    if request.method == "POST":
        data = request.POST
        task = Task.objects.create(
            task=data["task"],
        )

    return redirect("home")


def mark_as_done(request, id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=id)

        task.is_completed = True

        task.save()

    return redirect("home")


def delete_task(request, id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=id)
        task.delete()
    return redirect("home")


def edit_task(request, id):
    task = get_object_or_404(Task, id=id)
    form = TaskForm(instance=task)

    if request.method == "POST":
        data = request.POST

        form = TaskForm(instance=task, data=data)

        if form.is_valid():
            form.save()
            return redirect("home")

    return render(
        request,
        "edit-task.html",
        context={
            "form": form,
        },
    )


def undo_task(request, id):
    if request.method == "POST":
        task = Task.objects.get(id=id)

        task.is_completed = False

        task.save()

    return redirect("home")
