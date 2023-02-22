from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Multiuser(AbstractUser):
    email = models.EmailField()
    phone = models.IntegerField()
    is_manager = models.BooleanField(null=True)
    is_labour = models.BooleanField(null=True)

class Booklist(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    pdf = models.FileField(upload_to="book/pdf")
    cover = models.FileField(upload_to="book/cover")