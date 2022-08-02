from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return render(request, 'about.html', {'greting': 'Hello'})

def home(request):
    return HttpResponse('HOME')