import gensim, deepcut

def tokenize(string):
    return deepcut.tokenize(string)

def word_embedding(more_sentences):
    # Load & train word2vec model
    model = gensim.models.Word2Vec.load('/Users/AUM/Documents/PROJECT/mockup_senior_project/thai_text_mock_up/word2vec/w2v')
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
