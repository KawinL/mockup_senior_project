import re, glob, gensim, json
import sys
import os
from pymongo import MongoClient
sys.path.append(os.path.abspath(os.path.join('..')))
import word2vec

# Define MongoDB connection
client = MongoClient(port=27017)
db = client.pantip_data
collection = db.keyword_chula
all_sentences = []
for idx, post in enumerate(collection.find({})):
    # if (idx > 100):
    #     break
    tokenized_sentence = []
    title = post['title']
    topic = post['topic']
    comments = post['comments']

    tokenized_sentence = tokenized_sentence + word2vec.preprocessing.tokenize(title)
    tokenized_sentence = tokenized_sentence + word2vec.preprocessing.tokenize(topic)
    for comment in comments:
        if comment:
            tokenized_sentence = tokenized_sentence + word2vec.preprocessing.tokenize(comment)
        # print(comment)
    all_sentences.append(tokenized_sentence)
#
# print(all_sentences)
word_count = []
for idx, sentence in enumerate(all_sentences):
    for word in sentence:
        word_count.append(word)

print("Preprocessing data done!\n\tAll data : " + str(len(all_sentences)) + " sentences, " + str(len(word_count))
      + " words.")

# Train word2vec model for sentences
model = gensim.models.Word2Vec(all_sentences, min_count=1)
print("Training model done!")

# Save word2vec model
curfilePath = os.path.abspath(__file__)
curDir = os.path.abspath(os.path.join(curfilePath,os.pardir)) # this will return current directory in which python file resides.
model.save(curDir +'/chula_w2v.bin')