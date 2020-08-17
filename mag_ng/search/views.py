from django.shortcuts import render
from django.http import HttpResponse


def search(request):
    return HttpResponse('<h1>Search app</h1>')
