from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.reg, name='register'),

]

urlpatterns += staticfiles_urlpatterns()