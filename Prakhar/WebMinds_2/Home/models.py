from django.db import models

class SignUp(models.Model):
    email=models.EmailField(max_length=250)
    username=models.CharField(max_length=100)
    Contact=models.CharField(max_length=12)
    password=models.CharField(max_length=50)
