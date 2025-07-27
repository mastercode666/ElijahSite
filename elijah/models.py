from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    published_date = models.DateField(default=timezone.now)
    isbn_number = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField(default=0)
    cover_image = models.ImageField(upload_to='covers/')
    language = models.CharField(max_length=30)

    def __str__(self):
        return self.title
    

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    



class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} <{self.email}>"

