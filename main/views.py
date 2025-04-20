from django.shortcuts import render
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def index(request):
        return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def about_me(request):
    return render(request, 'main/about_me.html')

def error(request):
    with open('main/files/errors.txt', 'a') as file:
        file.write(f"[{datetime.now()}] 404 Not Found: {request.path}\n")
    return HttpResponseNotFound('404, page not found')

