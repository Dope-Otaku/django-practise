from django.shortcuts import render, HttpResponse
import datetime

def app2(request):
    return HttpResponse('This is app2')


def merry(request):
    now = datetime.datetime.now()
    return render(request, "po/merry.html", {
        "merry": now.day == 25 and now.month == 12
    })