from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest):
    print(request.path)
    print(request.headers)
    print(request.META)
    return HttpResponse("<h1>Hello, world.</h1>")