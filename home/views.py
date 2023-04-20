from django.shortcuts import render

""" Index Page View """


def index(request):
    return render(request, 'home/index.html')


def error_404(request, exception):
    return render(request, "404.html")


def error_500(request, *args, **kwargs):
    return render(request, "500.html", status=500)