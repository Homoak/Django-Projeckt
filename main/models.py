from django.db import models
from django.db.models import Model, CharField

class Produckt(models.Model):

    name = models.CharField(max_length=30)

    code = models.CharField(max_length=10)

class User(models.Model):
    user_name = models.CharField(max_length=50)

    email = models.CharField(max_length=100)

    password = models.CharField(max_length=50)

    age = models.IntegerField()

    phone = models.IntegerField()

    birthday = models.DateField()
