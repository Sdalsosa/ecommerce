from django.urls import path
from . import views

urlpatterns = [
    path('', views.prints, name='prints'),
    path('<int:pk>/', views.single_print, name='single_print'),
    path('add/', views.add_print, name='add_print'),
]
