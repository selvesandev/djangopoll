from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random


def home(request):
    """
    docstring
    """
    return render(request, 'home.html')
    # return HttpResponse("<h1>Hello this is my first django project.</h1>")
    pass


def passgen(request):
    """
    docstring
    """
    char = list('abcdefghijklmnopqrstuvwxyz0123456789#%^&*!@()')
    password = ""
    for x in range(16):
        password += random.choice(char)
    return render(request, 'passwordgen.html', {'password': password})
    # return JsonResponse({'password': password})
