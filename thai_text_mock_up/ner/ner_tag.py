import word2vec
from keras.models import load_model
import numpy as np
import os
from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import RepeatVector
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from keras.layers.wrappers import Bidirectional
TAG_LIST = ['DTM_I',
 'DES_I',
 'TRM_I',
 'DES_B',
 'BRN_I',
 'ABB_ORG_I',
 'BRN_B',
 'ORG_I',
 'PER_B',
 'LOC_B',
 'ABB_TTL_B',
 'ABB_DES_I',
 'TTL_B',
 'MEA_B',
 'NUM_B',
 'TRM_B',
 'MEA_I',
 'NUM_I',
 'ABB_B',
 'TTL_I',
 'ABB_LOC_B',
 'PER_I',
 'LOC_I',
 'ABB_LOC_I',
 'ABB_ORG_B',
 'O',
 'NAME_B',
 'ABB_DES_B',
 'DTM_B',
 'ORG_B',
'ABB_TTL_I','__','X']
def predict(sentences_vector):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    max_review_length = 106
    padded_text = sequence.pad_sequences(sentences_vector, maxlen=max_review_length)
    model = load_model(BASE_DIR+'/ner/ner003.h5')
    print(BASE_DIR)
    dummy = model.predict(padded_text)
    result = []
    print(padded_text)
    for i in range(len(sentences_vector[0])):
        print(TAG_LIST[np.argmax(dummy[0][i])])
        result.append(TAG_LIST[np.argmax(dummy[0][i])])
    print(result)
    return result


