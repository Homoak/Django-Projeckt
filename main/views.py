from django.shortcuts import render
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .forms import ContactForm

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

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
    else:
        form = ContactForm()

    return render(request, 'main/forms.html', {'form': form})

