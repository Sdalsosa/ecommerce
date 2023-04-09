from django.urls import path
from . import views

urlpatterns = [
    path('', views.prints, name='prints'),
    path('<pk>', views.single_print, name='single_print'),
]
