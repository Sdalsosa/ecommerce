from django.urls import path
from . import views

urlpatterns = [
    path('', views.prints, name='prints'),
    path('<int:pk>/', views.single_print, name='single_print'),
    path('add/', views.add_print, name='add_print'),
    path('edit/<int:pk>/', views.edit_print, name='edit_print'),
    path('delete/<int:pk>/', views.delete_print, name='delete_print'),
]
