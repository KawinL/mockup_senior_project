import gensim, deepcut

def tokenizr(string):
    new_sentences = deepcut.tokenize(string)
    return new_sentences

def word_embedder(sentence_list):
    # Load & train word2vec model
    model = gensim.models.Word2Vec.load('/Users/AUM/Documents/PROJECT/mockup_senior_project/thai_text_mock_up/preprocessing/w2v')
    # model.build_vocab(more_sentences)
    # model.train(more_sentences)
    sentence_vectors = []
    for word in sentence_list:
        try:
            wordVector = model[word]
        except KeyError:
         print(word + " Not found!")
        else:
            sentence_vectors.append(wordVector)
    return sentence_vectors
