from django.db import models


# Create your models here.
class Account(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=80)
    ip = models.CharField(max_length=30)
    agent = models.TextField()
    created_at = models.DateTimeField(auto_created=True)