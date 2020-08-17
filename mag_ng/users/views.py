from django.shortcuts import render
from django.http import HttpResponse


def register(request):
    return HttpResponse('<h1>Users registration page</h1>')

