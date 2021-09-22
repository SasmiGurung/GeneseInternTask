from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'home.html')


def health_check(request):
    return HttpResponse("Application is in good condition")
