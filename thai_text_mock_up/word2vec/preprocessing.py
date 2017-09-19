import gensim, deepcut
import os
def tokenize(string):
    return deepcut.tokenize(string)

def word_embedding(more_sentences):
    # Load & train word2vec model
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model = gensim.models.Word2Vec.load(BASE_DIR+'/word2vec/w2v')
    model.build_vocab(more_sentences, update=True)
    model.train(more_sentences, total_examples=model.corpus_count, epochs=model.iter)
    sentence_vectors = []
    for sentence in more_sentences:
        for word in sentence:
            try:
                wordVector = model[word]
            except KeyError:
                continue
            else:
                sentence_vectors.append(wordVector)
    return sentence_vectors

def word_embedding2(sentence):
    # Load & train word2vec model
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model = gensim.models.Word2Vec.load(BASE_DIR+'/word2vec/w2v')
    model.build_vocab(sentence, update=True)
    model.train(sentence, total_examples=model.corpus_count, epochs=model.iter)
    sentence_vectors = []
    for word in sentence:
        try:
            wordVector = model[word]
        except KeyError:
            continue
        else:
            sentence_vectors.append(wordVector)
    return sentence_vectors

