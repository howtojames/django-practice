from django.db import models

# Create your models here.
class User(models.Model):
    first_name=models.CharField(max_length=254)
    last_name=models.CharField(max_length=254)
    #want emails to be unique
    email=models.EmailField(max_length=254, unique=True)
