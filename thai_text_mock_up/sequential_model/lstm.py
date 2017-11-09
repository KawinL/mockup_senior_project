import os
from keras.models import model_from_json
from keras.preprocessing import sequence
import numpy as np
def predict(input):
    # load json and create model
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_file = open(BASE_DIR+'/sequential_model/beauty_review_pos_neg4.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    # load weights into new model
    loaded_model.load_weights(BASE_DIR+'/sequential_model/beauty_review_pos_neg4.h5')
    X_test = sequence.pad_sequences(np.array(input), maxlen=1000)
    neg_prob = str(loaded_model.predict(X_test)[0][0])
    neu_prob = str(loaded_model.predict(X_test)[0][1])
    pos_prob = str(loaded_model.predict(X_test)[0][2])
    print('pos : ',pos_prob)
    print('neg : ',neg_prob)
    return 'Negative '+neg_prob+'\tPositive '+pos_prob+'\tNeutral '+neu_prob