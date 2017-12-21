from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("<em>My second app</em>")


def help(request):
    params = dict()
    params["help"] = "this is help"
    return render(request, 'app_two/help.html', params)

