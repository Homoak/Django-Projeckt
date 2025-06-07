from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Produckt, Review, Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProducktForm(forms.ModelForm):
    class Meta:
        model = Produckt
        fields = ['name', 'price', 'description', 'category', 'image']

class ProducktFormReview(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'review']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'birth_date', 'avatar']

