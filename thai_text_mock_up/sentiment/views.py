from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, "input.html")


def analysis(request):
    print(type(request))
    text = request.GET.get('text')
    context = {
        'text': text,
        'rating': 100000
    }
    return render(request, "output.html", context)
