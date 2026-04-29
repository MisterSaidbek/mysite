from timeit import default_timer
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    products = [
        ('laptop', 2199),
        ('desktop', 3000),
        ('phone', 500)
    ]
    context = {
        "time_run": default_timer(),
        'products': products
    }

    return render(request, "myresume/myresume-index.html", context=context)