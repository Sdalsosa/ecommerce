from django.urls import path
from . import views

urlpatterns = [
    path('contactus/', views.contactus, name='contactus'),
    path('about/', views.about, name='about'),
    path('messages/', views.contactus_messages, name='messages'),
    path('single_message/<int:pk>', views.single_message, name='single_message'),
    path('delete_message/<int:pk>', views.delete_message, name='delete_message'),
]