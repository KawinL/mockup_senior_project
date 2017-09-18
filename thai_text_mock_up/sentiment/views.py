from django.shortcuts import render
from django.http import HttpResponse
import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))
import word2vec
# Create your views here.


def home(request):
    return render(request, "input.html")


def analysis(request):
    print(type(request))
    text = request.GET.get('text')
    context = {}
    tokenized_sentences = word2vec.preprocessing.tokenize(text)
    sentences_vector = word2vec.preprocessing.word_embedding(tokenized_sentences)
    context['tokenized'] = tokenized_sentences
    context['vector'] = sentences_vector
    return render(request, "output.html", context)
