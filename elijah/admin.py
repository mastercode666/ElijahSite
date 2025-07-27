from django.contrib import admin
from .models import Book, Article, ContactMessage

admin.site.site_header = "Elijahd Admin"
admin.site.site_title = "Elijahd Admin Portal"
admin.site.index_title = "Welcome to Elijahd Admin Portal"

# Register your models here.
admin.site.register(Book)
admin.site.register(Article)
admin.site.register(ContactMessage)


