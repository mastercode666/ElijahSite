from django.shortcuts import render
from .models import Book, Article, ContactMessage
from django.shortcuts import redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

# Create your views here.
def base(request):
    Articles = Article.objects.all().order_by('-published_date')[:3]
    return render(request, "home.html", {'articles': Articles})

def home(request):
    Articles = Article.objects.all().order_by('-published_date')[:3]
    return render(request, "home.html", {'articles': Articles})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def books(request):
    books = Book.objects.all()
    return render(request, "books.html", {'books': books})

def videos(request):
    return render(request, "videos.html")

from django.contrib import messages

@csrf_exempt
def contact_view(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        message= request.POST.get('message')

        #send email logic here
        send_mail(
            subject=f"New message from {name}",
            message=message,
            from_email=email,
            recipient_list=['erimarioeasy@gmail.com']
        )
        messages.success(request, "Your message has been sent successfully!")
        return redirect("contact")
    return render(request, "contact.html")