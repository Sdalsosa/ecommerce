from django.shortcuts import render

""" Index Page View """

def index(request):
    return render(request, 'home/index.html')