from django.shortcuts import render
from django.http import HttpResponse
import sys
import os
sys.path.append(os.path.abspath(os.path.join('..')))
import word2vec
import sequential_model
import numpy as np
# from .sequential_model.lstm import *
# Create your views here.


def home(request):
    return render(request, "input.html")


def analysis(request):
    print(type(request))
    text = request.GET.get('text')
    # print(text)
    context = {}
    tokenized_sentences = word2vec.preprocessing.tokenize(text)
    print(tokenized_sentences)
    sentences_vector = word2vec.preprocessing.word_embedding(tokenized_sentences)
    # print(sentences_vector)
    prediction= sequential_model.lstm.predict([sentences_vector])
    # context['tokenized'] = tokenized_sentences
    # context['vector'] = sentences_vector
    context['text'] = text
    context['rating'] = prediction
    return render(request, "output.html", context)

# def analysis2(text):
#     context = {}
#     tokenized_sentences = word2vec.preprocessing.tokenize(text)
#     print(tokenized_sentences)
#     sentences_vector = word2vec.preprocessing.word_embedding2(tokenized_sentences)
#     print(str(len(sentences_vector)))
#     prediction= sequential_model.lstm.predict([sentences_vector])
#     # context['tokenized'] = tokenized_sentence
#     # context['vector'] = sentences_vector
#     context['text'] = prediction
# <<<<<<< HEAD
# #     return prediction
# =======
# #     return prediction
# >>>>>>> 2ecd877917e89f1f50cdad1a4181092ee3eac000
