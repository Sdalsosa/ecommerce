from django.urls import path
from . import views

urlpatterns = [
    path('likes/<int:pk>/', views.like, name='like_print'),
]