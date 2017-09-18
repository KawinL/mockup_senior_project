import gensim, deepcut

def tokenize(string):
    return deepcut.tokenize(string)

def word_embedding(sentence_list):
    # Load & train word2vec model
    model = gensim.models.Word2Vec.load('/Users/AUM/Documents/PROJECT/mockup_senior_project/thai_text_mock_up/word2vec/w2v')
    # model.build_vocab(more_sentences)
    # model.train(more_sentences)
    sentence_vectors = []
    for word in sentence_list:
        try:
            wordVector = model[word]
        except KeyError:
            continue
        else:
            sentence_vectors.append(wordVector)
    return sentence_vectors
