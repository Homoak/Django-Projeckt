from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .forms import RegisterForm, ProducktForm, ProducktFormReview
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from .models import Basket, Produckt, Review

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

def index(request):
    products = Produckt.objects.all()    
    return render(request, 'main/index.html', {'products': products})

def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'main/reviews.html', {'reviews':reviews})

def shop(request):
    query = request.GET.get('q')
    if query:
        search = Produckt.objects.filter(name=query)
    else:
        search = Produckt.objects.all()
    products = Produckt.objects.all()    
    return render(request, 'main/shop.html', {'searchs':search, 'query':query, 'products': products})

def about(request):
    return render(request, 'main/about.html')

def about_me(request):
    return render(request, 'main/about_me.html')

def error(request):
    with open('main/files/errors.txt', 'a') as file:
        file.write(f"[{datetime.now()}] 404 Not Found: {request.path}\n")
    return HttpResponseNotFound('404, page not found')
        
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main/index.html')
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form})

def login_p(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"login_form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("index")

def add_to_cart(request):
    if request.method == 'POST':
        stuff_id = request.POST.get('stuff_id')
        person_id = request.POST.get('person_id')
        Basket.objects.create(stuff_id=stuff_id, person_id=person_id)
    return redirect('index')  

def add_produckt(request):
    if request.method == 'POST':
        form = ProducktForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
            form = ProducktForm()
    return render(request, 'main/admin_page.html', {'form': form})

def add_produckt_review(request):
    if request.method == 'POST':
        form = ProducktFormReview(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
            form = ProducktFormReview()
    return render(request, 'main/add_review.html', {'form': form})

# def search(request):
#     query = request.GET.get('q')
#     print(query)
#     if query:
#         search = Produckt.objects.filter(name=query)
#     else:
#         search = Produckt.objects.all()
        
#     print(search)
#     return render(request, 'main/search.html', {'searchs':search, 'query':query})
