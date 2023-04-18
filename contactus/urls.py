from django.urls import path
from . import views

urlpatterns = [
    path('contactus/', views.contactus, name='contactus'),
    path('about/', views.about, name='about'),
]