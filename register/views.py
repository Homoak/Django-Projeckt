from django.shortcuts import render
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def reg(request):
        return render(request, 'reg.html')


def error(request):
    with open('main/files/errors.txt', 'a') as file:
        file.write(f"[{datetime.now()}] 404 Not Found: {request.path}\n")
    return HttpResponseNotFound('404, page not found')