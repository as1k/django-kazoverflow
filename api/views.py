from django.http.request import HttpRequest
from django.http.response import HttpResponse


def hello(request):
    return HttpResponse('hello world')
