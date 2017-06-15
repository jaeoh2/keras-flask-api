import numpy as np
from keras.models import model_from_json
from skimage.io import imread, imshow
from skimage.transform import resize

import tensorflow as tf

def init():
    with open("model.json","r") as json_file:
        model_json = json_file.read()
    
    model = model_from_json(model_json)
    model.load_weights("model.h5")
    print("Loaded Model from disk")
    
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    
    graph = tf.get_default_graph()
    
    return model, graph
                 
    
    