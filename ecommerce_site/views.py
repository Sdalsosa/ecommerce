from django.shortcuts import render


def error404(request, exception):
    return render(request, '404.html', status=404)
