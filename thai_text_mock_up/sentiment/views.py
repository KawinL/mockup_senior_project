from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, "input.html")


def analysis(request):
    print(type(request))
    return HttpResponse(request.GET.get('text'))
