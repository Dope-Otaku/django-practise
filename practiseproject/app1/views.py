from django.shortcuts import render, HttpResponse


def app1(request):
    return render(request, 'lo/index.html')


def souvik(request):
    return HttpResponse("this is souvik")

def name(request, name):
    return render(request, "lo/greet.html", {
        "name": name.capitalize()
    })

