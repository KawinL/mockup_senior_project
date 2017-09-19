import os
from keras.models import model_from_json
from keras.preprocessing import sequence
import numpy as np
def predict(input):
    # load json and create model
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_file = open(BASE_DIR+'/sequential_model/model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    # load weights into new model
    loaded_model.load_weights(BASE_DIR+'/sequential_model/model.h5')
    X_test = sequence.pad_sequences(np.array(input), maxlen=500)
    return loaded_model.predict(X_test)[0][0]