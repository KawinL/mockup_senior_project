from django.shortcuts import render
from django.http import HttpResponse
import sys
import os
sys.path.append(os.path.abspath(os.path.join('..')))
import word2vec
import numpy as np
import ner
# from .sequential_model.lstm import *
# Create your views here.


def home(request):
    return render(request, "ner.html")

def analysis(request):
    text = request.GET.get('text')
    print(text)
    tokenized_sentences = word2vec.preprocessing.tokenize(text)
    sentences_vector = word2vec.preprocessing.word_embedding(tokenized_sentences)
    print(sentences_vector)
    prediction= ner.ner_tag.predict([sentences_vector])

    context = {}
    context['text'] = text
    context['rating'] = prediction
    context['token'] = tokenized_sentences
    return render(request, "ner.html", context)
