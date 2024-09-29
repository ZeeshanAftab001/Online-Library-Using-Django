from django.contrib import admin
from .models import Book,category

# Register your models here.

admin.site.register(Book)
admin.site.register(category)