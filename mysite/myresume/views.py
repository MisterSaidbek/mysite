from timeit import default_timer
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    context = {
        "time_run": default_timer(),
    }

    return render(request, "myresume/myresume-index.html", context=context)