from django.contrib import admin
from .models import Category, Print

# Register your models here.
admin.site.reguster(Category)
admin.site.reguster(Print)