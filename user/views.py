from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def register(request):
    return HttpResponse("<h1>Welcome to Django</h1>")