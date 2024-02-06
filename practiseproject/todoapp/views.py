from django.shortcuts import render

# Create your views here.
def todo(request):
    task = ["hello", "ball", "cat"]
    return render(request, "todo/todo.html", {
        "tasks": task
    })


def add(request):
    return render(request, "todo/add.html")