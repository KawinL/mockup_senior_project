import word2vec
from keras.models import load_model

def predict(sentences_vector):
    max_review_length = 106
    padded_text = sequence.pad_sequences(sentences_vector, maxlen=max_review_length)
    model = load_model('ner003.h5')
    dummy = model.predict(padded_text)
    for i in range(max_review_length):
        result.append(TAG_LIST[padded_text[i],np.argmax(dummy[0][i])])
    print(result)
    return result


