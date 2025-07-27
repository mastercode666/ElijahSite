from django.urls import path
from .import views

urlpatterns = [
    path("", views.base, name="base"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("books/", views.books, name="books"),
    path("videos/", views.videos, name="videos"),
    path("contact_view/", views.contact_view, name="contact_view"),
]