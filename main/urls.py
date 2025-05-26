from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about' ),
    path('about_me/', views.about_me, name='about_me'),
    path('404/', views.error, name='404' ),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_p, name='login'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart')
]
urlpatterns += staticfiles_urlpatterns()