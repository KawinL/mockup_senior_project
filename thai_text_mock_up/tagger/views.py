# -*- coding: utf-8 -*-
from django.shortcuts import render
import deepcut
import time
# Create your views here.

print("run before")


def home(request):
    return render(request, "taggerin.html")


def analysis(request):
    print(type(request))
    text = request.GET.get('text')
    text_list = [text, 'awertaqergqaerhgerthaethaethhth']
    text_list = deepcut.tokenize(text)
    print(text_list)
    text = '|'.join(text_list)
    context = {'text': text}
    return render(request, "taggerout.html", context)
